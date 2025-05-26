import subprocess
import psycopg2

#functia de mai jos basically ma ajuta sa citesc un query drept un string
def read_sql(file_path: str) -> str:
    with open(file_path, "r") as file:
        query = file.read()
        return query


#functia de mai jos implica sa execut cu ajutorul unui cursor query-ul citit
def execute_query(sql: str) -> None:
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
    # sql_query = read_sql("./Data Warehouse Arhitecture/silver/src/tables/create_subscription_plan_table.sql")
    # execute_query(sql_query)
    # subprocess.run(["python", "./ETL pipeline/src/transform/Subscription_plan_data.py"])

    query_paths = [
        # "./Data Warehouse Arhitecture/silver/src/sequences/user_id_sequence.sql",
        # "./Data Warehouse Arhitecture/silver/src/tables/create_dim_user_table.sql",
        # "./Data Warehouse Arhitecture/silver/src/tables/insert_dim_user_table.sql"
        # "./Data Warehouse Arhitecture/silver/src/tables/create_dim_reactions.sql",
        # "./Data Warehouse Arhitecture/silver/src/tables/insert_dim_reactions.sql"
        # "./Data Warehouse Arhitecture/silver/src/sequences/table_id_sequence.sql",
        # "./Data Warehouse Arhitecture/silver/src/tables/create_dim_titles.sql",
        # "./Data Warehouse Arhitecture/silver/src/tables/insert_dim_titles.sql"
        ]
    for query_path in query_paths:
        sql_query = read_sql(query_path)
        execute_query(sql_query)