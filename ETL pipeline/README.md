## Extract process

- Data is extracted from the `WoWCinema Platform`, `Netflix Movies and TV Shows (Kaggle)`, `IMDb Non-Commercial Datasets`.
- The script `./bronze/src/extract/WoWcinema.py` handles the "extraction" (more correctly the generation) of synthetic data.
- The script `./bronze/src/extract/Netflix_kaggle_data.py` handles the extraction of data from the Netflix movies Kaggle dataset.
- The script `./bronze/src/extract/IMDb_noncom_basiscs.py` handles the extraction of data from the IMDb non-comercial datasets, in concordance with the license of the source1.
- The script `./bronze/src/extract/IMDb_noncom_rating.py` handles the extraction of data from the IMDb non-comercial datasets, in concordance with the license of the source2.
- The script `./bronze/src/extract/Subscription_plan_data.py` handles the inserting of data into subscription plan table. (hardcoded the values unfortunately)
