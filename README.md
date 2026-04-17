# ✈️ Airflow Transaction Processing Pipeline

A production-ready transaction processing pipeline built with Apache Airflow that simulates real-time financial transaction processing. The pipeline automatically ingests, validates, detects fraud, processes payments, and generates reports every 10 minutes inside a Dockerized environment.

---

## 📌 Project Overview

This project simulates a real-world transaction pipeline that runs automatically every 10 minutes using Apache Airflow DAGs.

---

## 🔄 Pipeline Flow

```
ingest → validate → detect_fraud → process_payments → generate_report
```

| Task | Description |
|------|-------------|
| `ingest` | Fetches 10 random transactions with ID and amount |
| `validate` | Checks all transactions are valid |
| `detect_fraud` | Flags suspicious transactions randomly |
| `process_payments` | Processes and settles approved payments |
| `generate_report` | Prints final summary of the pipeline run |

---

## 🖼️ Screenshots

### DAG Graph - All tasks success
(<img width="3803" height="1813" alt="Screenshot 2026-04-17 164604" src="https://github.com/user-attachments/assets/cc25f331-cca1-409d-8f45-a33989debabe" />
)

### Gantt Chart - Tasks execution timeline
(<img width="3834" height="1644" alt="Screenshot 2026-04-17 164623" src="https://github.com/user-attachments/assets/b99a07bc-1998-411e-805f-b1f1649d6326" />
)

### DAG Details - 2 successful runs
(<img width="3804" height="1595" alt="Screenshot 2026-04-17 164541" src="https://github.com/user-attachments/assets/1a912144-8a0a-4805-97a4-f961d131feb6" />

)

### Task Duration Over Time
(<img width="3778" height="1669" alt="Screenshot 2026-04-17 164655" src="https://github.com/user-attachments/assets/dd0716b4-0ec2-4734-874d-e743f8cde5af" />
)

### Task Details
(<img width="3760" height="1796" alt="Screenshot 2026-04-17 164722" src="https://github.com/user-attachments/assets/4f287e01-b01e-430f-8795-440e37bcf533" />

)
---

## 🛠️ Tech Stack

- **Apache Airflow 2.7.1**
- **Docker & Docker Compose**
- **PostgreSQL** (Airflow backend)
- **Python 3.9**

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/airflow-pipeline.git
cd airflow-pipeline
```

**2. Start Docker containers**
```bash
docker-compose up -d
```

**3. Open Airflow UI**
```
http://localhost:8089
Username: admin
Password: admin
```

**4. Enable the DAG**
- Find `transaction_pipeline` in the UI
- Toggle it ON
- Watch it run every 10 minutes ✅

---

## 📁 Project Structure

```
airflow-pipeline/
│
├── dags/
│   └── Dags.py
│
├── screenshots/
│ 
├── depi.yml
├── requirements.txt
└── README.md
```

---
