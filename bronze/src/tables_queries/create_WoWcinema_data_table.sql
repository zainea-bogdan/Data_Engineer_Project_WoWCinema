create table if not exists bronze_wowcinema.wowcinema_data (
   log_id                  varchar(50),
   username                varchar(100),
   first_name              varchar(100),
   last_name               varchar(100),
   subscription_status     int,
   subscription_plan       int,
   subscription_start_date timestamp,
   iban                    varchar(45),
   title_name              varchar(255),
   watch_start_time        timestamp,
   watch_end_time          timestamp,
   session_duration_min    float,
   rating_given            float,
   reaction_type           int,
   country_code            varchar(3)
)