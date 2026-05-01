# -AI-System-Monitoring-Dashboard
A real-time system monitoring dashboard that tracks CPU, memory, and disk usage, predicts future CPU utilization using Machine Learning, and sends automated email alerts.

## 📌 Overview

This project simulates a **production-level monitoring system** similar to tools used in DevOps environments.  
It not only monitors system metrics but also applies **predictive analytics** and **automated alerting**.

---

## 🔥 Features

- 📊 Real-time CPU, Memory, Disk monitoring  
- 🤖 Machine Learning-based CPU prediction  
- 🚨 Threshold-based alert system  
- 📧 Automated email notifications (SMTP)  
- 🌐 REST APIs using Flask  
- ⚡ Live dashboard updates (JavaScript polling)  
- 🛡️ Alert throttling to prevent email spam  
- 🧩 Modular architecture using Flask Blueprints  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning:** Scikit-learn  
- **Monitoring:** psutil  
- **Email Service:** SMTP (Gmail App Password)  

---

## 📂 Project Structure


ai-system-monitor/
│── app/
│ ├── routes/
│ ├── services/
│ ├── models/
│ ├── utils/
│
│── ml/
│ ├── train.py
│ ├── predict.py
│ └── model.pkl
│
│── static/
│── templates/
│
│── run.py
│── requirements.txt
│── README.md


---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd ai-system-monitor
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python run.py

Open browser:

http://127.0.0.1:5000/
📬 Email Alert Setup
Enable 2-Step Verification in Gmail
Generate App Password
Update in:
app/utils/email_sender.py
sender = "your_email@gmail.com"
password = "your_app_password"
🧠 Machine Learning
Uses regression model to predict CPU usage
Combines real-time + predicted value for stability
Prevents unrealistic spikes (like 100% always)
🚨 Alert System
Triggered when CPU exceeds threshold
Sends email notification
Uses flag-based control to prevent repeated alerts
📸 Dashboard Preview
<img width="1112" height="245" alt="Screenshot 2026-04-27 221411" src="https://github.com/user-attachments/assets/9bce2cbe-a3f6-46d6-a654-b8762c556f83" />

🌐 Future Improvements
Cloud deployment (AWS / Render)
Advanced ML models (LSTM, Time Series)
Authentication system
Real-time streaming (Kafka)
