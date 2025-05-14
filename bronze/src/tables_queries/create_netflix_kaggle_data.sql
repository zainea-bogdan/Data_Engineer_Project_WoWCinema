create table if not exists bronze_wowcinema.netflix_kaggle_data (
   netf_title             varchar(255),
   netf_title_type        varchar(10),
   netf_director          varchar(255),
   netf_data_added        varchar(50),
   netf_release_year      int,
   netf_duration          varchar(25),
   netf_genre             varchar(255),
   netf_movie_description text
)