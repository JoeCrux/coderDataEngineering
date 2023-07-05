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
    #except Error as e:
    #    print(f"Error '{e}' ha ocurrido")

# conexion API
finnhub_client = finnhub.Client(api_key="bqoji3nrh5rced4gaukg")
# datos API
df =  pd.DataFrame(finnhub_client.company_earnings('TSLA', limit=5)) 

#constantes datos acceso a Redshift
hostname= 'data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com'
database= 'data-engineer-database'
username= 'jolcrux77_coderhouse'
pwd='180IXrK1xe'
port_id= '5439'

# Conexion a redshift
conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id)
args=""
for i in range(len(df)):
    if i == (len(df) - 1):
        args =args + str('(')+str(df.iloc[i]['actual'])+','+str(df.iloc[i]['estimate'])+','+"'"+str(df.iloc[i]['period'])+"'"+','+str(df.iloc[i]['quarter'])+','+str(df.iloc[i]['surprise'])+','+str(df.iloc[i]['surprisePercent'])+','+"'"+str(df.iloc[i]['symbol'])+"'"+','+str(df.iloc[i]['year'])+');'
    else:
        args =args + str('(')+str(df.iloc[i]['actual'])+','+str(df.iloc[i]['estimate'])+','+"'"+str(df.iloc[i]['period'])+"'"+','+str(df.iloc[i]['quarter'])+','+str(df.iloc[i]['surprise'])+','+str(df.iloc[i]['surprisePercent'])+','+"'"+str(df.iloc[i]['symbol'])+"'"+','+str(df.iloc[i]['year'])+'),'

query5="""INSERT INTO jolcrux77_coderhouse.company_earnings (actual,estimate,periodo,cuarto,surprise,surprisepercent,symbol,anio) VALUES """+ args

execute_query(conn, query5)
