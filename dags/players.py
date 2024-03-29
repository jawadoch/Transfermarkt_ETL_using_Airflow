from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from player import get_trans, print_done, transform, save_to_mongodb
import os


def to_csv_file(dataf):
    dag_file_path = os.path.abspath(__file__)
    csv_file_path = os.path.join(os.path.dirname(dag_file_path), 'players.csv')
    dataf.to_csv(csv_file_path, index=False)


default_args = {
    'owner': 'airflow',
    'start_date': datetime.now(),
    'schedule_interval': '@daily',
    'catchup': False,
}

dag = DAG(
    'data',
    default_args=default_args,
    description='DAG for scraping and saving transfermarkt data',
)


scrape_task = PythonOperator(
    task_id='get_trans',
    python_callable=get_trans,
    provide_context=True, 
    dag=dag,
)
transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    op_args=[scrape_task.output],  
    provide_context=True,
    dag=dag,
)

csv_task = PythonOperator(
    task_id='to_csv_file',
    python_callable=to_csv_file,
    op_args=[scrape_task.output],  
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='save_to_mongodb',
    python_callable=save_to_mongodb,
    op_args=[transform_task.output],  
    provide_context=True,
    dag=dag,
)

print_done_dag = PythonOperator(
    task_id='print_done',
    python_callable=print_done,
    provide_context=True,
    dag=dag,
)


scrape_task >> transform_task
scrape_task >> csv_task 
transform_task >> load_task
load_task >> print_done_dag

