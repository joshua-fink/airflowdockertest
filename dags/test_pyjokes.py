from airflow.decorators import dag, task
import pyjokes
import pendulum

@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 3, 20, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def test_pyjokes():

    @task()
    def print_jokes():
        print(pyjokes.get_joke())
        print(pyjokes.get_joke())


    print_jokes()

test_pyjokes()