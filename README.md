# Airflow-transaction-processing-pipeline
A production-ready transaction processing pipeline built with Apache Airflow that simulates real-time financial transaction processing. The pipeline automatically ingests, validates, detects fraud, processes payments, and generates reports every 10 minutes inside a Dockerized environment.
# ✈️ Airflow Transaction Processing Pipeline

A simulated transaction processing pipeline built with **Apache Airflow**, running inside **Docker**.

## 📌 Project Overview

This project simulates a real-world transaction pipeline that runs automatically every 10 minutes using Apache Airflow DAGs.
2. Start Docker containers
bash
docker-compose -f depi.yaml up -d
3. Open Airflow UI
text
http://localhost:8089
Username: admin
Password: admin
4. Enable the DAG
Find transaction_pipeline in the UI

Toggle it ON

Watch it run every 10 minutes ✅

📊 Sample Output
text
==================================================
TRANSACTION PIPELINE REPORT
==================================================
run_timestamp: 2026-04-17T14:30:00
total_transactions: 10
approved_count: 8
declined_count: 2
total_amount: 3421.50
total_fees: 85.54
net_amount: 3335.96
fraud_rate: 20.0
==================================================
📁 Project Structure
airflow-pipeline/
│
├── dags/
│   └── transaction_dag.py
│
├── screenshots/
│   ├── airflow_ui.png
│   ├── dag_graph.png
│   ├── tasks_running.png
│   └── task_logs.png
│
├── depi.yaml
├── requirements.txt
└── README.md
📝 DAG Configuration
Schedule: Every 10 minutes (*/10 * * * *)

Retries: 1 retry on failure

Start Date: January 1, 2024

Catchup: Disabled

🔧 Requirements
Create requirements.txt:

txt
apache-airflow==2.7.1
apache-airflow-providers-postgres==5.5.2
