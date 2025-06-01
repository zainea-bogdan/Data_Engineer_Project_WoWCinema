create table if not exists gold_wowcinema.cleaned_users_and_subscriptions (
   id_user                 int primary key,
   first_name              varchar(100) not null,
   last_name               varchar(100) not null,
   birth_date              date not null,
   iban                    varchar(60) not null,
   id_plan                 int not null,
   subscription_start_date date not null,
   subscription_plan       varchar(15) not null,
   subscription_price      float not null,
   currency_code           varchar(3) not null,
   discount_procentual     int not null
);

insert into gold_wowcinema.cleaned_users_and_subscriptions (
   id_user,
   first_name,
   last_name,
   birth_date,
   iban,
   id_plan,
   subscription_start_date,
   subscription_plan,
   subscription_price,
   currency_code,
   discount_procentual
)
   select distinct u.id_user,
                   u.first_name,
                   u.last_name,
                   u.birth_date,
                   u.iban,
                   u.id_plan,
                   u.subscription_start_date,
                   s.subscription_plan,
                   s.subscription_price,
                   s.currency_code,
                   s.discount_procentual
     from silver_wowcinema.dim_users u
     left join silver_wowcinema.dim_subscriptions s
   on u.id_plan = s.id_subscription
on conflict do nothing;

create table if not exists gold_wowcinema.cleaned_titles (
   id_title                  varchar(15) primary key,
   title_name                text not null,
   title_director_first_name varchar(100) not null,
   title_director_last_name  varchar(100) not null,
   title_type                varchar(100) not null,
   title_start_year          int not null,
   title_duration            int not null,
   title_rating              float not null,
   title_numvot_imdb         int not null
);

insert into gold_wowcinema.cleaned_titles (
   id_title,
   title_name,
   title_director_first_name,
   title_director_last_name,
   title_type,
   title_start_year,
   title_duration,
   title_rating,
   title_numvot_imdb
)
   select distinct id_title,
                   title_name,
                   title_director_first_name,
                   title_director_last_name,
                   title_type,
                   title_start_year,
                   title_duration,
                   title_rating,
                   title_numvot_imdb
     from silver_wowcinema.dim_titles
on conflict do nothing;


create table if not exists gold_wowcinema.cleaned_fact_table (
   id_log        varchar(50) primary key,
   id_user       int not null,
   id_title      varchar(15) not null,
   session_start timestamp not null,
   session_end   timestamp not null,
   rating_given  float not null,
   id_reaction   int not null,
   id_region     int not null,
   region_name   text not null,
   constraint fk_user_log foreign key ( id_user )
      references gold_wowcinema.cleaned_users_and_subscriptions ( id_user )
         on delete cascade,
   constraint fk_title_log foreign key ( id_title )
      references gold_wowcinema.cleaned_titles ( id_title )
         on delete cascade
);

insert into gold_wowcinema.cleaned_fact_table (
   id_log,
   id_user,
   id_title,
   session_start,
   session_end,
   rating_given,
   id_reaction,
   id_region,
   region_name
)
   select distinct f.id_log,
                   f.id_user,
                   f.id_title,
                   f.session_start,
                   f.session_end,
                   f.rating_given,
                   f.id_reaction,
                   f.id_region,
                   r.region_name
     from silver_wowcinema.fact_logs f
     left join silver_wowcinema.dim_regions r
   on f.id_region = r.id_region
   on conflict do nothing;