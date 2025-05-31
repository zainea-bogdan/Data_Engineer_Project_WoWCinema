insert into silver_wowcinema.dim_titles
select distinct 
btb.tconst,
btb.title,
case
when substring(bnb.primaryname,1,position(' ' in bnb.primaryname)) is null 
or substring(bnb.primaryname,1,position(' ' in bnb.primaryname)) = ' ' then 'Anonim_first_name'
else substring(bnb.primaryname,1,position(' ' in bnb.primaryname))
end,
case
when substring(bnb.primaryname,position(' ' in bnb.primaryname),length( bnb.primaryname)) is null
or  substring(bnb.primaryname,position(' ' in bnb.primaryname),length( bnb.primaryname)) = ' 'then 'Anonim_Last_name'
else substring(bnb.primaryname,position(' ' in bnb.primaryname),length( bnb.primaryname)) 
end,
btb.titletype,
cast(btb.startyear as integer),
case
when btb.runtime = '\N' then 0
else cast(btb.runtime as integer)
end,
btr.averagerating,
btr.numvotes
from bronze_wowcinema.title_basics as btb
left join bronze_wowcinema.title_crew btc on btb.tconst=btc.tconst
left join bronze_wowcinema.name_basics bnb on btc.director=bnb.nconst
left join bronze_wowcinema.title_ratings btr on btb.tconst=btr.tconst
where btb.tconst not in (select id_title from silver_wowcinema.dim_titles);