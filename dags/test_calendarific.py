# https://www.youtube.com/watch?v=Ai1ajkuZREE

from datetime import datetime
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor

country_codes = ['at', 'az', 'au', 'us']

def get_date() -> str:
    return str(datetime.now())

with DAG(
    dag_id='api_dag',
    schedule_interval='@daily',
    start_date=datetime(2024,3,20),
    catchup=False,
) as dag:

    task_is_api_active = HttpSensor(
        task_id='is_api_active',
        http_conn_id='calendar_api',
        endpoint='holidays/'
    )

    task_is_api_active

