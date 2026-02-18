# 🚀 Object Detection Using YOLO (Streamlit Web App)

A web-based Object Detection application built using **Ultralytics YOLO** and **Streamlit**.  
Users can upload an image, and the model detects objects with bounding boxes and confidence scores.

---

## 📌 Project Overview

This project demonstrates real-time object detection using a pretrained YOLO model integrated into a Streamlit web interface.

### Features:
- Upload image from local system
- Detect multiple objects
- Display bounding boxes with class labels
- Clean and simple UI

---

## 🛠 Tech Stack

- Python
- Streamlit
- Ultralytics YOLO
- OpenCV
- NumPy
- Pillow

---

## 📂 Project Structure
Object-Detection-YOLO/

│
├── app.py # Streamlit frontend
├── object_detect.py # YOLO detection logic
├── requirements.txt # Dependencies
└── README.md


---

## ⚙ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/object-detection-yolo.git
cd object-detection-yolo

### 2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install Required Packages
pip install -r requirements.txt

If requirements file is missing:
> pip install streamlit ultralytics opencv-python numpy pillow.

▶ Run the Application
streamlit run app.py
