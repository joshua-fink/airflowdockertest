import json

import pendulum

from airflow.decorators import dag, task

# this is a DAG definition file, serving as a configuration file for your pipeline

# This instantiates the DAG via @dag decorator, note function name is this case serves as the unique identifier
@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 3, 20, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def taskflow_api():
    """
    ### Taskflow API Tutorial Docs
    Simple data pipeline example which demonstrate use of Taskflow API using three simple tasks for ETL ops
    Find page of this example in Airflow Documentation: Tutorials/Working with TaskFlow
    """
    
    # Similar to @dag decorator, @task decorator ids the different tasks, with function name serving as the identifier
    @task()
    def extract():
        """
        #### Extract task
        Get data ready for rest of pipeline
        Simulate getting data by reading from hardcoded JSON string
        """
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'

        order_data_dict = json.loads(data_string)
        return order_data_dict

    # XCom variables still used behind the scenes, just abstracted away here with newer TaskFlow API
    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        """
        #### Transform task
        Takes in collection of order data and computes total order value
        """

        total_order_value = 0

        for value in order_data_dict.values():
            total_order_value += value

            return {"total_order_value": total_order_value}

    @task()
    def load(total_order_value: float):
        """
        #### Load task
        Takes in results of Transform task and prints it out instead of saving it to end user review
        """

        print(f"Total order value is: {total_order_value:.2f}")

    # task dependencies are automatically generated here based on functional invocation of tasks instead using
    # >>, chain, etc.
    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])

taskflow_api()
