insert into silver_wowcinema.dim_regions (
   id_region   ,
   region_name 
)values(%s,%s)
on conflict do nothing;