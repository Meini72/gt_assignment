from airflow import DAG
from airflow.utils.dates import days_ago
#from airflow.operators.mysql_operator import MySqlOperator
#from airflow.contrib.operators.bigquery_operator import BigQueryOperator
#from airflow.contrib.operators.bigquery_check_operator import BigQueryCheckOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from main import main


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['mnzhang72@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
}

dag = DAG(
    'gt_assignment',
    default_args=default_args,
    description='gt_assignment',
    schedule_interval=timedelta(hours=1))

# Config variables

task = PythonOperator(
    task_id='data_pipeline',
    python_callable=main,
    dag=dag,
)


task