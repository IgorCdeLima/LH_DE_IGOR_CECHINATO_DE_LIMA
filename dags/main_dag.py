from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
import pendulum
from scripts.estractor.data_lake import DataLake
from scripts.data_warehousing.postgre_loader import PostgreLoader


class MainDag:

    default_args = {
        'owner' : 'igor_c_lima',
        'depends_on_past' : True,
        'retries': 1,
        'retry_delay' : timedelta(minutes=5)
    }

    def __init__(self):
        pass

    def dag_start(self):
        local = pendulum.timezone('America/Sao_Paulo')

        with DAG(
            dag_id='lh_de_igor_cechinato_de_lima',
            default_args= self.default_args,
            start_date=pendulum.datetime(2025,1,1, tz=local),
            schedule_interval = "*/2 * * * *",
            catchup=False, 
            max_active_runs= 1,
            tags=['daily', 'banvic']
        ) as dag:
            
            extract_task_csv = PythonOperator(
                task_id= 'extract_transacoes_csv',
                python_callable = self.extract_transacoes_csv
            )
            extract_task_sql = PythonOperator(
                task_id = 'extract_tables_sql',
                python_callable = self.extract_tables_sql
            )

            data_lake_insert = PythonOperator(
                task_id = 'insert_data_lake',
                python_callable = self.insert_data_lake
            )

        [extract_task_csv, extract_task_sql] >> data_lake_insert
        return dag 
    
    def extract_transacoes_csv(self, **kwargs):
        data_lake = DataLake()
        address_csv = data_lake.csv_estractor()
        kwargs['ti'].xcom_push(key='address_csv', value=address_csv)

    
    
    def extract_tables_sql(self, **kwargs):
        data_lake = DataLake()
        address_tables = data_lake.sql_estractor()
        kwargs['ti'].xcom_push(key='address_tables', value=address_tables)
       
    def insert_data_lake(self, **kwargs):
        ti = kwargs['ti']
        addres_csv = ti.xcom_pull(key='address_csv', task_ids='extract_transacoes_csv' )
        addres_tables = ti.xcom_pull(key='address_tables', task_ids= 'extract_tables_sql')

        print(addres_csv)
        print(addres_tables)

