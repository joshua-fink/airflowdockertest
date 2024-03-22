# STEP 1: Import needed Python libraries

import textwrap
from datetime import datetime, timedelta

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator


# STEP 3: Create DAG object to nest tasks into,
with DAG(
    "fundamental_concepts", # string serves as unique identifier for the DAG
    
    # STEP 2: Define default args here (in this case belong to airflow.models.baseoperator.BaseOperator)
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        # Other params: 'queue', 'pool', 'priority_weight', 'end_date', 'wait_for_downstream', etc...
    },
    description = "Airflow tutorial in documentation: 'Tutorials/Fundamental Concepts'",
    schedule = timedelta(days=1),
    start_date = datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    # t1, t2, t3 are examples of tasks created by instantiating operators

    # STEP 4: Define tasks with operators. ALL OPERATORS inherit from BaseOperator, with specialization 
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )

    t1.doc_md = textwrap.dedent(
        """\
        #### Task Documentation
        You can document your task using the attributes `doc_md` (markdown)
        `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets rendered in UI's Task Instance Details page
        """
    )

    # There are other ways to do documentation

    # AIRFLOW ALLOWS JINJA TEMPLATING!
    templated_command = textwrap.dedent(
        """
        {% for i in range(5) %}
            echo "{{ ds }}"
            echo "{{ macros.ds_add(ds, 7) }}"
        {% endfor %}
        """
    )

    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=templated_command, # also can reference a file here, syntax like 'templated_command.sh'
    )

    t1 >> [t2, t3]

'''
This Python script is really just a configuration file specifying DAG's structure as code 
Actual tasks defined here run in separate context from script
Different tasks run on different workers at different points in time, so script cannot be used to cross communicate between tasks -> Xcoms solve this
NO DATA PROCESSING HERE! Needs to evaluate quickly so scheduler can execute it periodically to reflect any changes
'''