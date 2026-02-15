from airflow import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='monthly_first_monday_email',
    default_args=default_args,
    schedule_interval='0 9 * * 1#1',
    catchup=False,
    tags=['email', 'monthly'],
) as dag:

    send_email = EmailOperator(
        task_id='send_email_task',
        to='recipient@example.com',
        subject='Monthly Report',
        html_content="""
        <h3>Hello,</h3>
        <p>This is your monthly email sent on the first Monday.</p>
        """
    )

    send_email
