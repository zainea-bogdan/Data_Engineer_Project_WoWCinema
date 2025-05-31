insert into bronze_wowcinema.users (
   id_user                ,
   first_name              ,
   last_name              ,
   birth_date              ,
   subscription_plan      ,
   subscription_start_date ,
   iban                   
)
VALUES
(
     nextval('bronze_wowcinema.user_counter'),%s,%s,%s,%s,%s,%s
);