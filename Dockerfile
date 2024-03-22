FROM apache/airflow:2.8.1
ENV AIRFLOW_UID="airflow"
COPY requirements.txt .
RUN pip install -r requirements.txt