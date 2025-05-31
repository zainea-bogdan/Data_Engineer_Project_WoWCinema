import random

#the module below is used to create a connection with out local database
import psycopg2

#basically this statement from below i use it to extract from the whole library faker, just the class Faker
from faker import Faker

from datetime import timedelta


#functia de mai jos basically ma ajuta sa citesc un query drept un string
def read_sql(file_path: str) -> str:
    with open(file_path, "r") as file:
        query = file.read()
        return query
    
def execute_select_statement(sql:str)->list:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="placeholder",
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()


    return results

def execute_select_statement_conditioned(sql:str,data:list)->list:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="placeholder",
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute(sql,data)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results


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


def generate_synthetic_logs()->list:
    data=[]

    synthethic=Faker("ro_RO")

    #gen unique log id
    log_id = synthethic.uuid4()
    data.append(log_id)

    #select 1 id user
    read_sql_id_users=read_sql("./Data_Warehouse_Arhitecture/src/bronze/selecting/select_id_users.sql")
    list_id_user=execute_select_statement(read_sql_id_users)
    id_user_selectat=random.choice(list_id_user)[0]
    data.append(id_user_selectat)

    #select 1 title id
    read_sql_tconst=read_sql("./Data_Warehouse_Arhitecture/src/bronze/selecting/select_tconst_basics.sql")
    list_tconst=execute_select_statement(read_sql_tconst)
    id_title=random.choice(list_tconst)[0]
    data.append(id_title)

    #create a session start date, that isnt before the subscription plan start
    session_start=synthethic.date_time()

    #select subscription plan 
    id_user_necesar=[]
    id_user_necesar.append(id_user_selectat)
    subs_start_date_path="./Data_Warehouse_Arhitecture/src/bronze/selecting/select_subscription_start_date.sql"
    query_select_subscription_start_date = read_sql(subs_start_date_path)
    selected_subscription_plan=execute_select_statement_conditioned(query_select_subscription_start_date,id_user_necesar)[0][0]
    while session_start<selected_subscription_plan:
        session_start=synthethic.date_time()

    data.append(session_start)

    #create session_end
    adding_time = timedelta(minutes=random.randint(1,720)) 
    session_end = session_start + adding_time
    data.append(session_end)

    #rating
    rating = random.uniform(0,10)
    rating=round(rating,2)
    data.append(rating)

    #reaction type
    reaction_id=random.randint(-1,1)
    data.append(reaction_id)

    #region_code
    region_code=random.randint(1,42)
    data.append(region_code)



    return data




if __name__ =="__main__":  
    path_inserting="./Data_Warehouse_Arhitecture/src/bronze/inserting/insert_logs.sql"
    sql_insert=read_sql(path_inserting)
    for _ in range(300):
        data=generate_synthetic_logs()
        execute_insert_query(sql_insert,data)
        print("done")
    print("finish")