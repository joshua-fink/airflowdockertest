from airflow.decorators import dag, task
from colorama import Back, Fore, Style
import pendulum

@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 3, 20, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def test_colorama():

    @task()
    def print_stuff():
        print(Fore.RED + "some red text")
        print(Back.GREEN + "and with green background")
        print(Style.DIM + "and in dim text")

    print_stuff()

test_colorama()