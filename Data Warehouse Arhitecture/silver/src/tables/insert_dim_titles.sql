insert into silver_wowcinema.dim_titles (
   title_id,
   title_name,
   title_type,
   title_director,
   title_release_year,
   title_duration,
   title_genres,
   title_description
)
   select distinct nextval('title_id_counter') as title_id,
                   netf_title,
                   netf_title_type,
                   netf_director,
                   netf_release_year,
                   case
                      when netf_duration != 'NaN'
                         and cast(regexp_replace(
                         netf_duration,
                         '\s.*$',
                         ''
                      ) as integer) <= 9 then
                         cast(regexp_replace(
                            netf_duration,
                            '\s.*$',
                            ''
                         ) as integer) * 12 * 45
                      when netf_duration != 'NaN' then
                         cast(regexp_replace(
                            netf_duration,
                            '\s.*$',
                            ''
                         ) as integer)
                      else
                         null
                   end as duration_in_minutes,
                   netf_genre,
                   netf_movie_description
     from bronze_wowcinema.netflix_kaggle_data;