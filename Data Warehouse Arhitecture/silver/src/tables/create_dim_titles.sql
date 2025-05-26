create table if not exists silver_wowcinema.dim_titles (
   title_id           int primary key,
   title_name         varchar(255),
   title_type         varchar(50),
   title_director     varchar(255),
   title_release_year int,
   title_duration     float,
   title_genres       text,
   title_description  text
);