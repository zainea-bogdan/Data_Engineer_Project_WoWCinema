import random
import pandas as pd

#the module below is used to create a connection with out local database
import psycopg2



def extract_data_from_basiscs_tsv()->list:
    # i create a connection to our localserver to use it to acces our netflix table to extract 2 columns: titles and year
    conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="placeholder",
            host="localhost",
            port=5432
        )

    # taking data from netflix table
    # by using a cursor 
    cursor_tsv = conn.cursor()
    cursor_tsv.execute("SELECT netf_title, netf_release_year FROM bronze_wowcinema.netflix_kaggle_data")
    data1 = cursor_tsv.fetchall() #this line returns me a list of tuples
    cursor_tsv.close()

    # i created a key set called: "title_releaseYear", in order to optimize the isin() method from dataframe later
    title_key_set = {
        f"{title.replace(' ', '').lower()}_{str(release_year).strip()}"
        for title, release_year in data1
        if release_year
    }


    # 2. then i extract all data from the title.basics.tsv
    df1 = pd.read_csv(
        "IMDb/title.basics.tsv",
        sep="\t",
        usecols=["tconst", "primaryTitle", "titleType", "runtimeMinutes", "genres", "startYear"],
        dtype=str,
        on_bad_lines='skip'
    )

    # then i created in a similar method like above, a  cleaned title key without modifying original column
    df1["primaryTitle_clean"] = df1["primaryTitle"].str.replace(" ", "").str.lower()
    df1["startYear"] = df1["startYear"].str.strip()
    df1 = df1[df1["startYear"].notna()] # basically the inner part return a list of true and false => the outer df1[] keep the data where "startYear" exists (is true)

    df1["title_key"] = df1["primaryTitle_clean"] + "_" + df1["startYear"]

    # now we can do the matching based on title and release year
    filtered_data = df1[df1["title_key"].isin(title_key_set)]

    # then i am converting the filtered data into a list of tuplets
    final_data = list(filtered_data.itertuples(index=False, name=None))
    
 
    return final_data


#After completing the function for generating data, now we need to be able to load our generated data into our database
def load_data(data:list):
    conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="placeholder",
            host="localhost",
            port=5432
        )

    cursor = conn.cursor()

    sql = """
        insert into bronze_wowcinema.imdb_noncom_basiscs (
        imd_tconst         ,
        imd_primarytitle   ,
        imd_titletype     ,
        startyear ,
        imd_runtimeminutes ,
        imd_genres         
        )
        values(%s,%s,%s,%s,%s,%s)
        """
    
    for x in data:
        cursor.execute(
            sql,
            (x[0],x[2],x[1],x[3],x[4],x[5])
        )
    conn.commit()
        

if __name__ == "__main__":
    data=extract_data_from_basiscs_tsv()
    load_data(data)
