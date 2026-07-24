# ==========================
# IMPORTS
# ==========================
import csv
import os
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import cv2
from ultralytics import YOLO


# ==========================
# CONFIGURATION
# ==========================
MODEL_NAME = "yolov8n.pt"
CONFIDENCE = 0.5


def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "-q"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def load_model():
    try:
        return YOLO(MODEL_NAME)
    except Exception as exc:
        print(f"Installing ultralytics and retrying: {exc}")
        install_package("ultralytics")
        from ultralytics import YOLO as FreshYOLO
        return FreshYOLO(MODEL_NAME)


def resolve_video_source():
    candidates = []
    if len(sys.argv) > 1:
        candidates.append(Path(sys.argv[1]).expanduser())

    base_dir = Path(__file__).resolve().parent
    candidates.extend([
        base_dir / "video" / "human.mp4",
        base_dir / "human.mp4",
        Path("video") / "human.mp4",
        Path("human.mp4"),
    ])

    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def open_video_source():
    video_path = resolve_video_source()
    if video_path:
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened():
            print(f"Using video source: {video_path}")
            return cap

    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        print("Video file not found or unreadable; using webcam (0).")
        return cap

    raise RuntimeError("Unable to open any video source or webcam.")


def main():
    model = load_model()
    cap = open_video_source()

    # ==========================
    # STATISTICS
    # ==========================
    total_frames = 0
    total_objects = 0
    class_counter = defaultdict(int)

    base_dir = Path(__file__).resolve().parent
    output_video = str(base_dir / "output.mp4")
    csv_output = str(base_dir / "detections.csv")

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = int(cap.get(5)) or 20

    writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    show_window = os.environ.get("DISPLAY") is not None or os.name == "nt"

    with open(csv_output, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Frame", "Class", "Confidence"])

        start_time = time.time()

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            total_frames += 1

            results = model.predict(frame, conf=CONFIDENCE, verbose=False)
            boxes = results[0].boxes

            for box in boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                class_name = model.names[cls]

                class_counter[class_name] += 1
                total_objects += 1
                csv_writer.writerow([total_frames, class_name, round(conf, 2)])

            annotated = results[0].plot()
            current_time = time.time()
            fps_live = total_frames / (current_time - start_time) if current_time > start_time else 0.0

            cv2.putText(annotated, f"FPS: {fps_live:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(annotated, f"Objects: {len(boxes)}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            writer.write(annotated)

            if show_window:
                cv2.imshow("YOLOv8 Advanced Detector", annotated)
            if cv2.waitKey(1) == ord("q"):
                break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()

    print("\n========== REPORT ==========")
    print(f"Frames Processed : {total_frames}")
    print(f"Objects Detected : {total_objects}")

    for cls, count in sorted(class_counter.items()):
        print(f"{cls}: {count}")

    print("============================")


if __name__ == "__main__":
    main()
