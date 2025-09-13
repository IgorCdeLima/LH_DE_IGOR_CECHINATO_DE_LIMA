from scripts.estractor.data_lake import DataLake
from scripts.data_warehousing.postgre_loader import PostgreLoader


data_lake = DataLake()
address_csv = data_lake.csv_estractor()
address_tables = data_lake.sql_estractor()

sql_insert = PostgreLoader(address_csv, address_tables)

sql_insert.connect_postgresql()