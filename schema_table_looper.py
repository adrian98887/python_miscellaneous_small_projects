""" This code, given a query that returns the schema, table and column name. Loops through a Database and UNIONS the MAX(DATE) column, per each table, in each schema.
    It acts as a master table to monitor the last updated date/time.
"""



#pip install "snowflake-connector-python[pandas]"
import snowflake.connector
import pandas as pd
from snowflake.snowpark.session import *
from snowflake.connector.pandas_tools import write_pandas

#local path to login credentials
#%run /Users/adrianraszkiewicz/Desktop/snowflake/login.ipynb  

#for session connection
ctx = snowflake.connector.connect( 
    account= account,
    user=user,
    password= password,
    role= "",  
    warehouse= "",
    schema="",
    database=""
)  

cs = ctx.cursor() 

source_database= ''
target_database= ''
target_schema=''
target_table=''

#customize query as required
table_query = f"""            
select TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME 
from {source_database}.information_schema.columns 
where table_schema NOT IN ()
AND COLUMN_NAME IN ()  
AND (TABLE_NAME NOT LIKE '%%' AND TABLE_NAME NOT LIKE '')
"""

#Creates target table, executes query, loops through schemas/tables and appends to df. Then save to Snowflake.
def master_table(table_query):
    cs.execute(f"""
    CREATE OR REPLACE TABLE {target_database}.{target_schema}.{target_table}
    (TABLE_NAME VARCHAR, TABLE_SCHEMA VARCHAR, DATE VARCHAR)
    """)
    cs.execute(table_query)
    list = [x for x in cs.fetchall()]
    df1 = pd.DataFrame()
    
    for x in list:
        sql = f"SELECT '{x[1]}' as TABLE_NAME, '{x[0]}' as TABLE_SCHEMA, MAX({x[2]}) as DATE  FROM {source_database}.{x[0]}.{x[1]}"
        cs.execute(sql)
        df = cs.fetch_pandas_all()
        df1 = df1._append(df)
        
    df1['DATE']=df1['DATE'].astype(str)

    write_pandas(ctx, df1, target_table)
    
    
master_table(table_query)


