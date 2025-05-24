create table if not exists silver_wowcinema.fact_logs (
   user_id                 int primary key,
   username                varchar(100),
   first_name              varchar(100),
   last_name               varchar(100),
   birth_date              date,
   user_iban               varchar(45),
   region_code             int,
   subscription_start_date timestamp
);