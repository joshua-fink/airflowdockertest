# Airflow / Docker Test
By Joshua Fink (joshuafink@geico.com)

## 3/21/24: More DAGS, First Connection Fail

### Successes

**New: Use 'docker compose build' to run Dockerfile with extra Python packages**

<ul>
  <li> Figured out how to audit logs to find where statements in tasks were printed
  <li> Completed the 'Fundamental Concepts' tutorial in Airflow documentation ('dags/fundamental_concepts.py') </li>
  <li> Created DAG to test TaskFlow API for Docker in 'dags/taskflow_api.py' </li>
  <li> Learned how to share tasks between DAGS in same file ('dags/reuse_task_in_multiple_dags.py') and share tasks between files ('dags/use_task_in_other_file.py') </li>
  <li> Learned how to extend enviroment using 'Dockerfile', 'requirements.txt' to allow DAG to use 'pyjokes' package </li>
  <li> Learned how to create virtual environment local to task with 'randfacts' package in 'dags/testing_virtual_envs.py' </li>
</ul>

### Current Difficulties

<ul>
  <li> Tried to follow tutorial on Connections to set up Calendarific API via Airflow UI, got confused. Then tried running in via 'dags/test_calendarific.py'. A bit confused on how to properly set it up. Theory is permissions of account in Docker Container may not be configured properly. </li>
  <li> Currently, 'dags/test_calendarific.py' runs a test using 'HttpSensor()' operator to test if connection is active. DAG fails instead :( </li>
</ul>



## 3/20/24: Initial Setup
Defined first DAG inside 'dags/my_dag.py' and ran it successfully in Docker Container on personal Windows PC

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
