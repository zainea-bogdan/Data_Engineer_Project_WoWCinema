create table if not exists silver_wowcinema.dim_subscriptions (
   id_subscription     int primary key,
   subscription_plan   varchar(15),
   subscription_price  float,
   currency_code       varchar(3),
   discount_procentual int
)