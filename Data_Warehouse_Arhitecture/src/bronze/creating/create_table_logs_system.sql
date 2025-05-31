create table if not exists bronze_wowcinema.log_system (
   id_log        varchar(50),
   id_user       int,
   titleconst    varchar(15),
   session_start timestamp,
   session_end   timestamp,
   rating_given  float,
   reaction_type int,
   region_code   int
);