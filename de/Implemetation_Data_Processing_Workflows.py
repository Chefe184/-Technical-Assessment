from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'customer_data_load',
    default_args=default_args,
    description='Load customer data into the database',
    schedule_interval=None, # Set to None for a one-off trigger
)

def load_customer_data(ds, **kwargs):
    # Your logic to fetch and load customer data into the database goes here
    pass

load_task = PythonOperator(
    task_id='load_customer_data',
    provide_context=True,
    python_callable=load_customer_data,
    dag=dag,
)

load_task
