create table if not exists silver_wowcinema.dim_reactions (
   id_reaction   int primary key,
   reaction_name text unique
);