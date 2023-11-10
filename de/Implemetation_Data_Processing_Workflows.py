ffrom airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2

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
    schedule_interval=None,  # Set to None for a one-off trigger
)

def load_customer_data(ds, **kwargs):
    # Example logic to fetch and load customer data into the database
    # Replace 'your_data_source.csv' with your actual data source
    df = pd.read_csv('your_data_source.csv')

    # Database connection parameters
    conn_params = {
        'dbname': 'companydata',
        'user': 'admin',
        'password': 'admin',
        'host': 'localhost',
        'port': '5432'
    }

    # Connect to the database
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    # Insert data into the database
    # Replace 'your_table' with your actual table name and adapt the query as needed
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO your_table (column1, column2, ...) VALUES (%s, %s, ...)",
            (row['column1'], row['column2'], ...)
        )

    conn.commit()
    cursor.close()
    conn.close()

load_task = PythonOperator(
    task_id='load_customer_data',
    provide_context=True,
    python_callable=load_customer_data,
    dag=dag,
)

load_task

