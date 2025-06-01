-- /*Movie Completion Report*/
create or replace view gold_wowcinema.movie_completion_ratio_raport as
   select distinct round(
      avg(
         case
            when(
               case
                  when gct.title_duration = 0 then
                     1.0
                  else extract(epoch from gft.session_end - gft.session_start) /(gct.title_duration * 60.0)
               end
            ) > 1 then
               1.0
            else(case
               when gct.title_duration = 0 then
                  1.0
               else extract(epoch from gft.session_end - gft.session_start) /(gct.title_duration * 60.0)
            end)
         end
      ),
      3
   ) as avg_movie_completion_rate
     from gold_wowcinema.cleaned_fact_table gft
     left join gold_wowcinema.cleaned_titles gct
   on gft.id_title = gct.id_title;


-- /*Session Duration Report -avg time*/
create or replace view gold_wowcinema.average_time_spent_on_platform as
   select distinct round(
      avg((case
         when gct.title_duration = 0 then
            1.0
         else extract(epoch from gft.session_end - gft.session_start) / 360
      end)),
      0
   ) as average_session_duration
     from gold_wowcinema.cleaned_fact_table gft
     left join gold_wowcinema.cleaned_titles gct
   on gft.id_title = gct.id_title;


-- /*active vcs inactive user numbers */
create or replace view gold_wowcinema.act_inact_user_report as
   with user_activity as (
      select distinct gcu.id_user useru,
                      count(gft.id_log) as activity
        from gold_wowcinema.cleaned_fact_table gft
       right join gold_wowcinema.cleaned_users_and_subscriptions gcu
      on gcu.id_user = gft.id_user
       group by gcu.id_user
   )
   select case
             when activity > 0 then
                'active users'
             else
                'inactive users'
          end as status,
          count(*) number_of_users
     from user_activity
    group by status;

/*user distributions by plans*/
create or replace view gold_wowcinema.user_distribution_by_plan as
   select distinct subscription_plan,
                   count(id_user)
     from gold_wowcinema.cleaned_users_and_subscriptions
    group by subscription_plan;

/*Active vs. Inactive Users by Subscription Plan*/
create or replace view gold_wowcinema.active_and_inactive_users_by_subscription_plan as
   with user_activity as (
      select distinct gcu.id_user useru,
                      gcu.subscription_plan plan,
                      count(gft.id_log) as activity
        from gold_wowcinema.cleaned_fact_table gft
       right join gold_wowcinema.cleaned_users_and_subscriptions gcu
      on gcu.id_user = gft.id_user
       group by gcu.id_user
   )
   select plan,
          case
             when activity > 0 then
                'active users'
             else
                'inactive users'
          end as status,
          count(*) number_of_users
     from user_activity
    group by plan,
             status;

/*Revenue Analysis by Subscription Tier*/
create or replace view gold_wowcinema.revenue_per_subscription_tier as
   select distinct subscription_plan,
                   ( count(id_user) * subscription_price ) as revenue
     from gold_wowcinema.cleaned_users_and_subscriptions
    group by subscription_plan,
             subscription_price;


/*Top 10 Most Watched Movies*/
create or replace view gold_wowcinema.top_10_movie_watched as
select distinct
gct.id_title,
gct.title_name,
count(gft.id_log) number_of_views
from gold_wowcinema.cleaned_titles gct 
left join gold_wowcinema.cleaned_fact_table gft on gct.id_title=gft.id_title
group by gct.id_title,gct.title_name
order by number_of_views desc 
limit 10;

/*Bottom 10 Least Watched Movies*/
create or replace view gold_wowcinema.Bottom_10_Least_Watched_Movies as
select distinct
gct.id_title,
gct.title_name,
count(gft.id_log) number_of_views
from gold_wowcinema.cleaned_titles gct 
left join gold_wowcinema.cleaned_fact_table gft on gct.id_title=gft.id_title
group by gct.id_title,gct.title_name
order by number_of_views asc 
limit 10;

/*Platform vs. IMDb Rating Comparison*/
create or replace view gold_wowcinema.rating_comaprison_plat_imdb as
select distinct 
gct.title_name,
gct.title_rating as imdb_avg_rating,
case
when avg(gft.rating_given) is null then 0
else avg(gft.rating_given)
end platform_rating
from gold_wowcinema.cleaned_titles gct 
left join gold_wowcinema.cleaned_fact_table gft on gct.id_title=gft.id_title
group by gct.id_title,
gct.title_rating;