insert into silver_wowcinema.dim_users (
   user_id,
   username,
   first_name,
   last_name,
   birth_date,
   user_iban,
   region_code,
   subscription_start_date
)
   select distinct nextval('user_id_counter'),
                   username,
                   first_name,
                   last_name,
                   birth_date,
                   iban,
                   region_code,
                   subscription_start_date
     from bronze_wowcinema.wowcinema_data;