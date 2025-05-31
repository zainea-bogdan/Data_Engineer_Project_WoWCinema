create table if not exists silver_wowcinema.dim_users (
   id_user                 int primary key,
   first_name              varchar(100),
   last_name               varchar(100),
   birth_date              date,
   subscription_start_date date,
   iban                    varchar(60)
);