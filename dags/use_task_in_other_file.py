from reuse_task_in_multiple_dags import mr_worldwide_addition
from airflow.decorators import dag
from datetime import datetime

@dag(start_date=datetime(2024, 3, 20))
def use_mr_worldwide():
    start = mr_worldwide_addition.override(priority_weight=3)(1,2)
    for i in range(3):
        start >> mr_worldwide_addition.override(task_id=f"other_file_{i}")(start, i)
    
use_mr_worldwide_dag = use_mr_worldwide()