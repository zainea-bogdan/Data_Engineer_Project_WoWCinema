insert into silver_wowcinema.fact_logs
select distinct 
bls.id_log,
bls.id_user,
bls.titleconst,
bls.session_start,
bls.session_end,
bls.rating_given,
bls.reaction_type,
bls.region_code
from bronze_wowcinema.log_system as bls
inner join bronze_wowcinema.users bus on bls.id_user=bus.id_user
where bls.id_user not in (select id_user from silver_wowcinema.fact_logs);