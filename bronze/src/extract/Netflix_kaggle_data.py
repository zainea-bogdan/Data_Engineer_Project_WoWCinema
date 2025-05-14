import random
import pandas as pd


#the module below is used to create a connection with out local database
import psycopg2




def get_data_from_csv()->list:

    
    #making an empty list to store an synthethic generated entry
    data_rows=[]

    #now we create each part of our netflix_kaggle_data 
    df=pd.read_csv("bronze/data/netflix_titles.csv",sep=',')
    for i in df.itertuples():
        data=[]
        data.append(i[3])
        data.append(i[2])
        data.append(i[4])
        data.append(i[7])
        data.append(i[8])
        data.append(i[10])
        data.append(i[11])
        data.append(i[12])
        data_rows.append(data)
        
    

    return data_rows



#After completing the function for generating data, now we need to be able to load our generated data into our database
def load_data(data_rows:list):
    # We create a connection to our localserver where we need to complete each
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="placeholder",
        host="localhost",
        port=5432
    )

    cursor = conn.cursor()

    sql = """
        insert into  bronze_wowcinema.netflix_kaggle_data
        (
        netf_title             ,
        netf_title_type       ,
        netf_director          ,
        netf_data_added      ,
        netf_release_year     ,
        netf_duration         ,
        netf_genre            ,
        netf_movie_description 
        )
        values (%s,%s,%s,%s,%s,%s,%s,%s);
        """
        
    cursor.executemany(
        sql,
        data_rows
    )
    conn.commit()




if __name__ == "__main__":
    data_rows=get_data_from_csv()
    load_data(data_rows)
