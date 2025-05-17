create table if not exists bronze_wowcinema.subscription_plan (
   subscription_plan_id int,
   subscription_plan    varchar(15),
   subscription_price   float,
   currency_code        varchar(3)
)