import os
from decouple import config
import finnhub
import pandas as pd
import psycopg2
def execute_query(connection, query):
    cursor = connection.cursor()
    Error=""
    try:
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

# conexion API
finnhub_client = finnhub.Client(api_key="bqoji3nrh5rced4gaukg")

# datos API
df =  pd.DataFrame(finnhub_client.company_earnings('TSLA', limit=5)) 

#ordeno dataframe 
dforder = df.sort_values(['period', 'quarter'])

#constantes datos acceso a Redshift

hostname= config('hostname_red')
database= config('database_red')
username= config('username_red')
pwd= config('pwd_red')
port_id= config('port_id_red')

# Conexion a redshift
conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id)

# Armado de string de valores a insertar
args=""
for i in range(len(dforder)):
    if i == (len(dforder) - 1):
        args =args + str('(')+str(dforder.iloc[i]['actual'])+','+str(dforder.iloc[i]['estimate'])+','+"'"+str(dforder.iloc[i]['period'])+"'"+','+str(dforder.iloc[i]['quarter'])+','+str(dforder.iloc[i]['surprise'])+','+str(dforder.iloc[i]['surprisePercent'])+','+"'"+str(dforder.iloc[i]['symbol'])+"'"+','+str(dforder.iloc[i]['year'])+');'
    else:
        args =args + str('(')+str(dforder.iloc[i]['actual'])+','+str(dforder.iloc[i]['estimate'])+','+"'"+str(dforder.iloc[i]['period'])+"'"+','+str(dforder.iloc[i]['quarter'])+','+str(dforder.iloc[i]['surprise'])+','+str(dforder.iloc[i]['surprisePercent'])+','+"'"+str(dforder.iloc[i]['symbol'])+"'"+','+str(dforder.iloc[i]['year'])+'),'

#formateo comando sql
query5="""INSERT INTO jolcrux77_coderhouse.company_earnings (actual,estimate,periodo,cuarto,surprise,surprisepercent,symbol,anio) VALUES """+ args

#llamo a funcion para ejecutar comando sql
execute_query(conn, query5)

