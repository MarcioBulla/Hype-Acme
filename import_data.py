import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Boolean, Date, VARCHAR, Float
from sqlalchemy.schema import Table, MetaData, Column, ForeignKey
import os
import json

host = "mydb"

print("Preparando dados...")
path_ipca = os.path.join("data", "ipca.json")

path_exec = os.path.join("data", "executions.csv")
path_func = os.path.join("data", "functions.csv")

file_ipca = open(path_ipca)
json_ipca = json.load(file_ipca)
file_ipca.close()

for entities in json_ipca:
    for elements in entities['resultados']:
        for var in elements['series']:
            ipca_var = var['serie']

ano_mes, buying_power = [], []
for key, val in ipca_var.items():
    ano_mes.append(key)
    buying_power.append(val)

df_icpa = pd.DataFrame({"date": ano_mes, "buying_power": buying_power})
df_icpa["date"] = pd.to_datetime(df_icpa["date"], format="%Y%m") 

df_exec = pd.read_csv(path_exec)
df_func = pd.read_csv(path_func)

print("Concluido")

print("Connectando no docker...")
db = mysql.connector.connect(
    host=host, port=3306,
    user='root', password='acme')
print("connectado")


print("Criando DATABASES...")
db_cursor = db.cursor()

db_cursor.execute('CREATE DATABASE IF NOT EXISTS service')
db_cursor.execute('CREATE DATABASE IF NOT EXISTS ibge')
db_cursor.close()
db.close()
print("Concluido")


print("Criando TABLES...")
engine_1 = create_engine(
    "mysql+mysqlconnector://root:acme@"+host+":3306/ibge")
engine_23 = create_engine(
    "mysql+mysqlconnector://root:acme@"+host+":3306/service")


df_icpa.to_sql("ipca", con=engine_1, if_exists='replace', index=False, dtype={
    "date": Date ,
    "buying_power": Float()})

df_func.to_sql("functions", con=engine_23, if_exists='replace', index=False, dtype={
    "id": Integer ,
    "function_name": VARCHAR(20) ,
    "external_component_avg_latency": Integer,
    "has_external_component": Boolean})

df_exec.to_sql("executions", con=engine_23, if_exists='replace', index=False, dtype={
    "id": Integer, 
    "date": Date,
    "function_id": Integer, 
    "execution_time": Integer})

print("Concluido")
print("Definindo chaves...")


with engine_23.connect() as conn:
    conn.execute("""
    ALTER TABLE functions ADD PRIMARY KEY(id);
    """)

    conn.execute("""
    ALTER TABLE executions ADD PRIMARY KEY (id)
    """)
    conn.execute("""
    ALTER TABLE executions ADD FOREIGN KEY (function_id) REFERENCES functions(id)
    """)

print("Chaves definidas")
