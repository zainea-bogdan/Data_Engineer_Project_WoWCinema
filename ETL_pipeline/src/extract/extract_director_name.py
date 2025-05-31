import pandas as pd
#the module below is used to create a connection with out local database
import psycopg2

#basically this statement from below i use it to extract from the whole library faker, just the class Faker
from faker import Faker

import re

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

#I decided for quick iteration and prototyping to get the top 15000 movies by rating and numvotes
if __name__ =="__main__":  
    coduri=[]
    path_dir_names="./Data_Warehouse_Arhitecture/src/bronze/selecting/select_all_directors_codes_from_crew.sql"
    sql_query_directors_codes=read_sql(path_dir_names)
    getting_directors_codes = execute_select_statement(sql_query_directors_codes)
    for i in range(len(getting_directors_codes)):
        codurile_pe_bucati=re.split(r'[,,/s]+',getting_directors_codes[i][0])
        coduri.extend(codurile_pe_bucati)
    coduri_deduplicate=list(dict.fromkeys(coduri))

    title_directors_raw= pd.read_csv("./IMDb/name.basics.tsv",delimiter='\t',usecols=[0,1,2,3,5],na_values="\\N")  
    sql_path="./Data_Warehouse_Arhitecture/src/bronze/inserting/insert_title_director_names.sql"
    title_directors=title_directors_raw.fillna(value=0)
    title_directors['birthYear']=title_directors['birthYear'].astype(int)
    title_directors['deathYear']=title_directors['deathYear'].astype(int)
    wanted_directors = title_directors[
        title_directors['nconst'].isin(coduri_deduplicate)]
    sql_query=read_sql(sql_path)
    for row in wanted_directors.itertuples(index=False):
        rand=list(row)
        execute_insert_query(sql_query,rand)
        print("done")    
    print("finish")
