import pandas as pd
#the module below is used to create a connection with out local database
import psycopg2

#basically this statement from below i use it to extract from the whole library faker, just the class Faker
from faker import Faker

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

#I decided for quick iteration and prototyping to get the top 15000 movies by rating and numvotes
if __name__ =="__main__":  
    title_ratings=pd.read_csv("./IMDb/title.ratings.tsv",delimiter='\t',usecols=[0,1,2])
    title_ratings_sorted_15000_rows = title_ratings.sort_values(
    by=['numVotes','averageRating'],
    ascending=[False, False]).head(15000)

    sql_path="./Data_Warehouse_Arhitecture/src/bronze/inserting/insert_title_ratings.sql"
    sql_query=read_sql(sql_path)
    for row in title_ratings_sorted_15000_rows.itertuples(index=False):
        rand=list(row)
        execute_insert_query(sql_query,rand)
        print("done")    
    print("finish")
