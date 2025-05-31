create table if not exists silver_wowcinema.fact_logs (
   id_log          varchar(50) primary key,
   id_user         int
      references silver_wowcinema.dim_users ( id_user ),
   id_subscription int
      references silver_wowcinema.dim_subscriptions ( id_subscription ),
   id_title        varchar(15),
   session_start   timestamp,
   session_end     timestamp,
   rating_given    float,
   id_reaction     int
      references silver_wowcinema.dim_reactions ( id_reaction ),
   id_region       int
      references silver_wowcinema.dim_regions ( id_region )
);