# 👁️ Face, Eye & Smile Detection using OpenCV

This project demonstrates real-time **face, eye, and smile detection** using OpenCV’s Haar Cascade classifiers. It works on both **live webcam video** and **static images**.

---

## 🚀 Features

- 👤 Face detection
- 👀 Eye detection
- 😊 Smile detection
- 🎥 Real-time webcam detection
- 🖼️ Image-based detection (batch processing)
- 📦 Uses OpenCV Haar Cascades (no deep learning required)

---

## 🧠 How It Works

The project uses **Haar Cascade Classifiers** to detect features:

- Face → detected first from grayscale frames
- ROI (Region of Interest) is extracted from detected face
- Eyes and smile are detected inside that ROI

---

## ⚙️ Installation

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

--- 

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/face-eye-smile-detection.git
cd face-eye-smile-detection
```

--- 

## ▶️ Usage

### 🎥 Real-Time Webcam Detection

```bash
python video_detect.py
```

- Press Q to exit the webcam window

---

### 🖼️ Image Detection

```bash
python photo_detect.py
```

- Processes all images inside Sample Pictures/
- Displays detection results one by one

---

### 🎯 Features

- Face detection using Haar Cascades
- Eye detection within face region
- Smile detection within face region
- Works on both images and real-time video
- Lightweight and fast (no GPU needed)

---

### 🖥️ Output Behavior
- 🟩 Green rectangle → Face detected
- Labels shown:
    + Eye Detected / Eye Not Detected
    + Smile Detected / Smile Not Detected

---

### 🛠️ Tech Stack

- Python 🐍
- OpenCV 👁️
- Haar Cascade Classifiers

---

### 👨‍💻 Author

Roshan Karki
AI/ML Learner🚀

---

### 📜 License

This project is open-source and free to use for learning purposes.