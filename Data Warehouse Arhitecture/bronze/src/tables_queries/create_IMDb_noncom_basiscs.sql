create table if not exists bronze_wowcinema.imdb_noncom_basiscs (
   imd_tconst         varchar(20),
   imd_primarytitle   varchar(255),
   imd_titletype      varchar(25),
   startyear          int,
   imd_runtimeminutes varchar(50),
   imd_genres         text
)