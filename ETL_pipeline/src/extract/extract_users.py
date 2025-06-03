import random

#the module below is used to create a connection with out local database
import psycopg2

#basically this statement from below i use it to extract from the whole library faker, just the class Faker
from faker import Faker

def generate_synthetic_data_users()->list:
    data=[]
    synthethic=Faker("ro_RO")
    #user id il generez cu o secventa
    first_name = synthethic.first_name()
    data.append(first_name)
    last_name =synthethic.last_name()
    data.append(last_name)
    birth_date= synthethic.date_time()
    data.append(birth_date)
    subscription_plan =random.randint(1,3)
    data.append(subscription_plan)
    subscription_start_date = synthethic.date_time()
    while (subscription_start_date < birth_date or subscription_start_date.year < 2024):
        subscription_start_date = synthethic.date_time()
    data.append(subscription_start_date)
    iban = synthethic.iban()
    data.append(iban)

    return data


#functia de mai jos basically ma ajuta sa citesc un query drept un string
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
    user_insert_sql="./Data_Warehouse_Arhitecture/src/bronze/inserting/insert_users.sql"
    sql_query = read_sql(user_insert_sql)
    for i in range(40):
        data=generate_synthetic_data_users()
        execute_insert_query(sql_query,data)
        print("done")

