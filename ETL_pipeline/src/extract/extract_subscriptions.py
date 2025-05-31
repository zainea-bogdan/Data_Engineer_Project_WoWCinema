#library for connectors to postgreSQL
import psycopg2

#functia de mai jos basically ma ajuta sa citesc un query drept un string
def read_sql(file_path: str) -> str:
    with open(file_path, "r") as file:
        query = file.read()
        return query

#functia de mai jos implica sa execut cu ajutorul unui cursor query-ul citit pentru structura
def execute_structural_query(sql: str) -> None:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="placeholder",
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ =="__main__":  
    query_paths_structure = [
        "./Data_Warehouse_Arhitecture/src/bronze/inserting/insert_subscriptions.sql",
        ]
    for query_path in query_paths_structure:
        sql_query = read_sql(query_path)
        execute_structural_query(sql_query)
        print("done")

 


