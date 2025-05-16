import random
import pandas as pd


#the module below is used to create a connection with out local database
import psycopg2




#basically this statement from below i use it to extract from the whole library faker, just the class Faker
from faker import Faker

#basically this statement from below i use it in order to use from datetime module the timedelta class - that helps me add time durations to a date_time object, and the result to remain date_time
from datetime import timedelta


# we declare this function in order to generate synthethic data for our WoWcinema_data, mentioned in Readme.md
def generate_synthethic_data()->list:
    #we create an instance of the Faker class, and we sent as parameter the "ro_RO", to make sure that the generator give result in Romanian
    synthethic=Faker("ro_RO")
    
    #making an empty list to store an synthethic generated entry
    data=[]

    #now we create each part of our Wowcinema_data "table"
    
    log_id = synthethic.uuid4()
    data.append(log_id)
    username=synthethic.user_name()
    data.append(username)
    first_name = synthethic.first_name()
    data.append(first_name)
    last_name =synthethic.last_name()
    data.append(last_name)
    subscription_status = random.randint(0,1)
    data.append(subscription_status)
    subscription_plan =random.randint(1,3)
    data.append(subscription_plan)
    subscription_start_date = synthethic.date()
    data.append(subscription_start_date)
    iban = synthethic.iban()
    data.append(iban)

    #reading the titles from netflix dataset to get some movies the 
    get_titles = pd.read_csv("bronze/data/netflix_titles.csv",sep=',',usecols=["title"])

    make_title_unique=get_titles["title"].unique()

    title_list=list(make_title_unique)


    title_name=random.choice(title_list)
    data.append(title_name)


    watch_start_time = synthethic.date_time()
    #making sure that we don t have users that watched before the platform was even made:))
    while(watch_start_time.year<2000):
         watch_start_time = synthethic.date_time()

    data.append(watch_start_time)

    #the context for creating the watch_end_time
    #so if a user let's says it watches a 90 minutes movie, 
    #but the difference between the watch end and start time si greater than movie length, 
    # that means in that log was captured time spent by user on our platform scrolling too 
    # (like the time scrolling between movies/serials = (watch_start_time - watch_end_time)-movie_length) - if positive of course
    # if the difference this ((watch_start_time - watch_end_time)-movie_length) is <0  that means that the movie wasn't seen completed-and the log was closed
    #ex: i decided to add watchtime between 1minute up to 360, decided random per log
    adding_time = timedelta(minutes=random.randint(1,360)) 
    watch_end_time = watch_start_time + adding_time

    data.append(watch_end_time)

    session_duration_min = (watch_end_time-watch_start_time).total_seconds()/60

    data.append(session_duration_min)
    
    rating_given = round(random.uniform(0,10),2)
    data.append(rating_given)

    reaction_type = random.randint(-1,1)
    data.append(reaction_type)
    
    country = synthethic.country_code()
    data.append(country)
    

    return data



#After completing the function for generating data, now we need to be able to load our generated data into our database
def load_data(data:list):
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
        Insert into bronze_wowcinema.wowcinema_data
        (
        log_id                  ,
        username                ,
        first_name              ,
        last_name             ,
        subscription_status    ,
        subscription_plan       ,
        subscription_start_date ,
        iban                    ,
        title_name              ,
        watch_start_time        ,
        watch_end_time          ,
        session_duration_min    ,
        rating_given            ,
        reaction_type           ,
        country_code            
        )
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ;
        """
        
    cursor.execute(
        sql,
        (
            data[0], data[1], data[2], data[3], data[4], data[5], data[6],
            data[7], data[8], data[9], data[10], data[11], data[12],data[13],
            data[14]
        )
    )
    conn.commit()




if __name__ == "__main__":
    for _ in range(100):
        mock_data=generate_synthethic_data()
        load_data(mock_data)
