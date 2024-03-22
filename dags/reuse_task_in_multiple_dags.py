from airflow.decorators import task, dag
from datetime import datetime

@task
def mr_worldwide_addition(x, y):
    print(f"Task args: x={x}, y={y}")
    return x + y

@dag(start_date=datetime(2024, 3, 20))
def sharedag1():
    start = mr_worldwide_addition.override(task_id="start")(1, 2)
    for i in range(3):
        start >> mr_worldwide_addition.override(task_id=f"start_{i}")(start, i)


@dag(start_date=datetime(2024, 3, 20))
def sharedag2():
    start = mr_worldwide_addition(1, 2)
    for i in range(3):
        start >> mr_worldwide_addition.override(task_id=f"s2_{i}")(start, i)

sharedag1_dag = sharedag1()
sharedag2_dag = sharedag2()