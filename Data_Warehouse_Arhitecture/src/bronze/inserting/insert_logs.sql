insert into bronze_wowcinema.log_system (
   id_log      ,
   id_user       ,
   titleconst   ,
   session_start ,
   session_end   ,
   rating_given ,
   reaction_type ,
   region_code  
)values(%s,%s,%s,%s,%s,%s,%s,%s);