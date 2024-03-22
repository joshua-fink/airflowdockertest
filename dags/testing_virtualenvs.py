from airflow.decorators import dag, task
import pendulum

@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 3, 20, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def testing_virtualenvs():

    @task.virtualenv(
        requirements="randfacts==0.21.0"
    )
    def print_python_fact():

        import randfacts

        print(randfacts.get_fact())
        print(randfacts.get_fact())


    print_python_fact()

testing_virtualenvs()