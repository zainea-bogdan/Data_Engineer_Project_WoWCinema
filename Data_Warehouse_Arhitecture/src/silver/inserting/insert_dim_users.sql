insert into silver_wowcinema.dim_users
select 
blu.id_user,
blu.first_name,
blu.last_name,
date(blu.birth_date),
date(blu.subscription_start_date),
blu.iban
from bronze_wowcinema.users as blu
where blu.id_user not in (select id_user from silver_wowcinema.dim_users);