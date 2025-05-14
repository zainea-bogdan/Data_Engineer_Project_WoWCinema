select *
  from bronze_wowcinema.netflix_kaggle_data; /*but in postgres is limited to 1000*/

/*run this to make sure you have all the movies*/
select count(*)
  from bronze_wowcinema.netflix_kaggle_data;