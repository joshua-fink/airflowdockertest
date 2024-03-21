# Airflow / Docker Test
Defined first DAG inside 'dags/my_dag.py' and ran it successfully in Docker Container

### Helpful Tutorials
After running into a few dead ends, these YouTube videos ended up being the most helpful:
<ul>
  <li> How to Install Apache Airflow on Windows using Docker Container (https://www.youtube.com/watch?v=4gz9SogFh1Q)
  <li> Airflow DAG: Coding your first DAG for Beginners (https://www.youtube.com/watch?v=IH1-0hwFZRQ) </li>
</ul>

#### Comments from How to Install Apache Airflow on Windows using Docker Container video (very helpful)
How to Install Apache Airflow on Windows using Docker Container 

1. create a directory named airflow and inside that create three sub directories - logs, dags, plugins and place docker-compose.yaml file inside airflow directory
2. install docker desktop for windows
3. download docker-compose.yaml file of airflow latest release
[https://airflow.apache.org/docs/apach...](https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml)

Airflow releases: [https://airflow.apache.org/docs/apach...](https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html#airflow-2-8-1-2024-01-19)

4. docker-compose up airflow-init
5. docker-compose up

Cleanup - below command will delete all the conainer and free up the volumes and memory
`Run docker-compose down --volumes --remove-orphans`
command in the directory you downloaded the docker-compose.yaml file

airflow-scheduler - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.
airflow-webserver - The webserver is available at http://localhost:8080.
airflow-worker - The worker that executes the tasks given by the scheduler.
airflow-triggerer - The triggerer runs an event loop for deferrable tasks.
airflow-init - The initialization service.
postgres - The database.
redis - The redis - broker that forwards messages from scheduler to worker.


![image](https://github.com/joshua-fink/airflowdockertest/assets/49216284/02b07ee2-0d8b-489d-9084-c078138b2d7c)
