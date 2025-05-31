create table if not exists bronze_wowcinema.users (
   id_user                 int,
   first_name              varchar(100),
   last_name               varchar(100),
   birth_date              timestamp,
   subscription_plan       int,
   subscription_start_date timestamp,
   iban                    varchar(60)
);