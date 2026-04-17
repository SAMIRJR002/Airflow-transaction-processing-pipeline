from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random
import json

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'transaction_pipeline',
    default_args=default_args,
    description='Transaction processing pipeline runs every 10 minutes',
    schedule_interval='*/10 * * * *',
    catchup=False,
    tags=['transactions', 'pipeline']
)

def ingest(**context):
    transactions = []
    for i in range(10):
        trans = {
            'id': f'TX{datetime.now().strftime("%Y%m%d%H%M%S")}{i}',
            'amount': round(random.uniform(10, 1000), 2),
            'user_id': random.randint(1, 100),
            'timestamp': datetime.now().isoformat()
        }
        transactions.append(trans)
    
    context['ti'].xcom_push(key='transactions', value=transactions)
    print(f"Ingested {len(transactions)} transactions")
    return f"Ingested {len(transactions)} transactions"

def validate(**context):
    transactions = context['ti'].xcom_pull(key='transactions', task_ids='ingest')
    valid = []
    invalid = []
    
    for trans in transactions:
        if trans['amount'] > 0:
            valid.append(trans)
        else:
            invalid.append(trans)
    
    context['ti'].xcom_push(key='valid_transactions', value=valid)
    print(f"Validated: {len(valid)} valid, {len(invalid)} invalid")
    
    if invalid:
        raise ValueError(f"Found {len(invalid)} invalid transactions")
    
    return f"Validated {len(valid)} transactions"

def detect_fraud(**context):
    transactions = context['ti'].xcom_pull(key='valid_transactions', task_ids='validate')
    
    for trans in transactions:
        trans['is_fraud'] = random.random() < 0.1
        if trans['amount'] > 800:
            trans['is_fraud'] = True
    
    fraud_count = sum(1 for t in transactions if t['is_fraud'])
    context['ti'].xcom_push(key='checked_transactions', value=transactions)
    
    print(f"Fraud detection complete: {fraud_count} fraudulent transactions found")
    return f"Found {fraud_count} fraudulent transactions"

def process_payments(**context):
    transactions = context['ti'].xcom_pull(key='checked_transactions', task_ids='detect_fraud')
    
    approved = []
    declined = []
    
    for trans in transactions:
        if trans['is_fraud']:
            trans['status'] = 'declined'
            declined.append(trans)
        else:
            trans['status'] = 'approved'
            trans['processing_fee'] = trans['amount'] * 0.025
            approved.append(trans)
    
    context['ti'].xcom_push(key='approved_transactions', value=approved)
    context['ti'].xcom_push(key='declined_transactions', value=declined)
    
    total_approved = sum(t['amount'] for t in approved)
    print(f"Processed payments: {len(approved)} approved (${total_approved}), {len(declined)} declined")
    
    return f"Approved: {len(approved)}, Declined: {len(declined)}"

def generate_report(**context):
    approved = context['ti'].xcom_pull(key='approved_transactions', task_ids='process_payments')
    declined = context['ti'].xcom_pull(key='declined_transactions', task_ids='process_payments')
    
    total_amount = sum(t['amount'] for t in approved)
    total_fees = sum(t.get('processing_fee', 0) for t in approved)
    net_amount = total_amount - total_fees
    
    report = {
        'run_timestamp': datetime.now().isoformat(),
        'total_transactions': len(approved) + len(declined),
        'approved_count': len(approved),
        'declined_count': len(declined),
        'total_amount': round(total_amount, 2),
        'total_fees': round(total_fees, 2),
        'net_amount': round(net_amount, 2),
        'fraud_rate': round(len(declined) / (len(approved) + len(declined)) * 100, 2)
    }
    
    report_file = f'/data/report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "="*50)
    print("TRANSACTION PIPELINE REPORT")
    print("="*50)
    for key, value in report.items():
        print(f"{key}: {value}")
    print("="*50 + "\n")
    
    context['ti'].xcom_push(key='final_report', value=report)
    return f"Report generated: {report_file}"

ingest_task = PythonOperator(
    task_id='ingest',
    python_callable=ingest,
    dag=dag
)

validate_task = PythonOperator(
    task_id='validate',
    python_callable=validate,
    dag=dag
)

fraud_task = PythonOperator(
    task_id='detect_fraud',
    python_callable=detect_fraud,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_payments',
    python_callable=process_payments,
    dag=dag
)

report_task = PythonOperator(
    task_id='generate_report',
    python_callable=generate_report,
    dag=dag
)

ingest_task >> validate_task >> fraud_task >> process_task >> report_task