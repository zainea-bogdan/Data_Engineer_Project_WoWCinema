create table if not exists silver_wowcinema.dim_titles (
   id_title                  varchar(15),
   title_name                text,
   title_director_first_name varchar(100),
   title_director_last_name  varchar(100),
   title_type                varchar(100),
   title_start_year          int,
   title_duration            int,
   title_rating              float,
   title_numvot_imdb         int
);