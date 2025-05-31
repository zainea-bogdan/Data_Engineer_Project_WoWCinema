import pandas as pd
#the module below is used to create a connection with out local database
import psycopg2

def read_sql(file_path: str) -> str:
    with open(file_path, "r") as file:
        query = file.read()
        return query

#functia de mai jos implica sa execut cu ajutorul unui cursor query-ul citit
def execute_insert_query(sql: str,data:list) -> None:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="placeholder",
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute(sql,data)
    conn.commit()
    conn.close()


if __name__ =="__main__":  
    data=pd.read_csv("./Data_Warehouse_Arhitecture/src/silver/creating/judete_romania.txt",usecols=[0,1])
    data['id']=data['id'].astype(int)
    sql_query = read_sql("./Data_Warehouse_Arhitecture/src/silver/inserting/insert_dim_regions.sql")
    for row in data.itertuples(index=False):
        list_elem=list(row)
        execute_insert_query(sql_query,list_elem)
        print("done")
    print("finish")

