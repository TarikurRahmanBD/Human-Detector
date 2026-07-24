<div align="center">
  <h1>👤 Human Detector | YOLOv8 Object Analytics & Logger</h1>
  <p>Real-time object detection engine with automated CSV telemetry logging and annotated video export.</p>
  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.12+-blue?style=flat&logo=python" alt="Python 3.12+" />
    </a>
    <a href="https://github.com/ultralytics/ultralytics">
      <img src="https://img.shields.io/badge/YOLOv8-✅-blue?style=flat" alt="YOLOv8" />
    </a>
    <a href="https://opencv.org/">
      <img src="https://img.shields.io/badge/OpenCV-4.x+-blue?style=flat&logo=opencv" alt="OpenCV" />
    </a>
    <a href="https://pandas.pydata.org/">
      <img src="https://img.shields.io/badge/Pandas-✅-blue?style=flat&logo=pandas" alt="Pandas" />
    </a>
    <a href="/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="MIT License" />
    </a>
    <a href="#-open-source-collaboration--call-for-contributors">
      <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat" alt="PRs Welcome" />
    </a>
  </p>
</div>

---

## 🌟 Overview & Quick Summary

`human_detector` detects objects and humans from video or webcam streams, logs detections into `detections.csv`, overlays live FPS and active object counts, and exports annotated output to `output.mp4`.

---

## 🔥 Key Features

- 📊 **Automated CSV telemetry logging**
  - Stores per-frame detection data in `detections.csv`
- 🎥 **Annotated video output recorder**
  - Saves processed footage into `output.mp4`
- ⏱️ **Real-time FPS & Active Object counter**
  - Displays live performance and detection counts on screen
- 📈 **Post-execution statistical summary**
  - Prints frame totals, object totals, and class distribution after exit

---

## 🛠️ Tech Stack & Dependencies

- Python 3.12+
- OpenCV
- Ultralytics YOLOv8
- Pandas

Install dependencies:

```powershell
pip install opencv-python ultralytics pandas
```

---

## 🚀 How to Run Locally

```powershell
git clone https://github.com/tarikurrahmanbd/YOLO_Projects-main.git
cd YOLO_Projects-main/human_detector
python human_detector.py
```

---

## 👨‍💻 Developer & Lead Engineer

**Designed & Developed by Tarikur Rahman**

GitHub: [TarikurRahmanBD](https://github.com/TarikurRahmanBD)

---

## 🤝 Open-Source Collaboration & Call for Contributors

Contributions are welcome to expand this project with features like:

- Web UI dashboards (Streamlit / Gradio)
- Database integration for detection telemetry
- Automated email alert systems for object events

---

## 📄 License & Attribution

This project is licensed under the **MIT License**.

**Designed & Developed by Tarikur Rahman**
