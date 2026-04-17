✈️ Airflow Transaction Processing Pipeline
A simulated transaction processing pipeline built with Apache Airflow, running inside Docker.

📌 Project Overview
This project simulates a real-world transaction pipeline that runs automatically every 10 minutes using Apache Airflow DAGs.

🔄 Pipeline Flow
ingest → validate → detect_fraud → process_payments → generate_report
Task	Description
ingest	Fetches 10 random transactions with ID and amount
validate	Checks all transactions are valid
detect_fraud	Flags suspicious transactions randomly
process_payments	Processes and settles approved payments
generate_report	Prints final summary of the pipeline run
🖼️ Screenshots
