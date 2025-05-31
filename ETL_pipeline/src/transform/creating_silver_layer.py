#library for connectors to postgreSQL
import psycopg2
import subprocess

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
        "./Data_Warehouse_Arhitecture/src/schemas/create_silver_schema.sql",
        "./Data_Warehouse_Arhitecture/src/silver/creating/create_dim_users.sql",
        "./Data_Warehouse_Arhitecture/src/silver/inserting/insert_dim_users.sql",
        "./Data_Warehouse_Arhitecture/src/silver/creating/create_dim_titles.sql",
        "./Data_Warehouse_Arhitecture/src/silver/inserting/insert_dim_titles.sql",
        "./Data_Warehouse_Arhitecture/src/silver/creating/create_dim_subscriptions.sql",
        "./Data_Warehouse_Arhitecture/src/silver/inserting/insert_dim_subscriptions.sql",
        "./Data_Warehouse_Arhitecture/src/silver/creating/create_dim_regions.sql",
        "./Data_Warehouse_Arhitecture/src/silver/creating/create_dim_reactions.sql",
        "./Data_Warehouse_Arhitecture/src/silver/inserting/insert_dim_reactions.sql",
        "./Data_Warehouse_Arhitecture/src/silver/creating/create_table_fact_logs.sql",
        "./Data_Warehouse_Arhitecture/src/silver/inserting/insert_fact_logs.sql"
        ]
    for query_path in query_paths_structure:
        sql_query = read_sql(query_path)
        execute_structural_query(sql_query)
        print("done")

    subprocess.run(["python", "./ETL_pipeline/src/transform/dim_region.py"])
 


