from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
from scripts.data_lake import DataLake


def extract_transacoes_csv(ti):
    data = DataLake()
    address_csv = data.csv_estractor()
    ti.xcom_push(key='address_csv', value=address_csv)

def extract_tables_sql(ti):
    data = DataLake()
    address_tables = data.sql_estractor()
    ti.xcom_push(key='address_tables', value=address_tables)
    
def insert_data_lake(ti):
    address_csv = ti.xcom_pull(key='address_csv', task_ids='extract_transacoes_csv')
    address_tables = ti.xcom_pull(key='address_tables', task_ids='extract_tables_sql')
    print(address_csv, address_tables)  

        

with DAG(
    dag_id='lh_de_igor_cechinato_de_lima',
    start_date=pendulum.datetime(2025,1,1),
    schedule= "*/5 * * * *",
    catchup=False, 
    max_active_runs= 1,
    tags=['benvic']
) as dag:
            
    extract_task_csv = PythonOperator(
        task_id= 'extract_transacoes_csv',
        python_callable = extract_transacoes_csv
    )
    extract_task_sql = PythonOperator(
        task_id = 'extract_tables_sql',
        python_callable = extract_tables_sql
    )

    data_lake_insert = PythonOperator(
        task_id = 'insert_data_lake',
        python_callable = insert_data_lake
    )

([extract_task_csv, extract_task_sql] >> data_lake_insert)
    

