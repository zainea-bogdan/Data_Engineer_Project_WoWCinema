create table if not exists bronze_wowcinema.title_basics (
   tconst    varchar(15),
   titletype varchar(100),
   title     text,
   isadult   text,
   startyear text,
   runtime   text,
   genres    text
);