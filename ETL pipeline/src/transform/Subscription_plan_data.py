import random

#the module below is used to create a connection with out local database
import psycopg2


#After completing the function for generating data, now we need to be able to load our generated data into our database
def load_data():
    # We create a connection to our localserver where we need to complete each
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="placeholder",
        host="localhost",
        port=5432
    )

    cursor = conn.cursor()

    sql_1 = """
    insert into silver_wowcinema.subscription_plan (
    subscription_plan_id ,
    subscription_plan    ,
    subscription_price   ,
    currency_code       
    )
    values (1,'Basic',4.99,'USD')
        """
        
    cursor.execute(sql_1)
    conn.commit()
    
    sql_2 = """
    insert into silver_wowcinema.subscription_plan (
    subscription_plan_id ,
    subscription_plan    ,
    subscription_price   ,
    currency_code       
    )
    values (2,'Standard',9.99,'USD')
        """
        
    cursor.execute(sql_2)

    conn.commit()

    sql_3 = """
    insert into silver_wowcinema.subscription_plan (
    subscription_plan_id ,
    subscription_plan    ,
    subscription_price   ,
    currency_code       
    )
    values (3,'Premium',13.99,'USD')
        """
        
    cursor.execute(sql_3)

    conn.commit()




if __name__ == "__main__":
    load_data()
