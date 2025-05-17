import pandas as pd
import psycopg2

def extract_data_from_IDMb_ratings():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="placeholder",
        host="localhost",
        port=5432
    )

    data=[]
    cursor_reading_from_netflix = conn.cursor()
    cursor_reading_from_netflix.execute("select imd_tconst from  bronze_wowcinema.imdb_noncom_basiscs")
    for x in cursor_reading_from_netflix.fetchall():
        data.append(x[0])
    cursor_reading_from_netflix.close()
    set_data=set(data)

    df1=pd.read_csv(
        "IMDb/title.ratings.tsv",
        sep='\t',
        usecols= ['tconst', 'numVotes', 'averageRating'],
        dtype=str,
        on_bad_lines='skip'
    )

    filtred_frame=df1[df1["tconst"].isin(set_data)]
    list_filtrata=list(filtred_frame.itertuples(index=False, name=None))

    return list_filtrata
    



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
    insert into bronze_wowcinema.imdb_noncom_ratings (
        imd_tconst       ,
        imd_averagerating ,
        imd_numvotes      
        )
    values (%s,%s,%s)
        """
        
    for x in data:
        cursor.execute(
            sql,
            (x[0], x[1], x[2])
        )
    conn.commit()




if __name__ == "__main__":
    data=extract_data_from_IDMb_ratings()
    load_data(data)

