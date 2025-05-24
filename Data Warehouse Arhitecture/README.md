# Data Warehouse Arhitecture

It has a server `WoWCinema` and a database named `WoWCinema`; and for movies details it was decided to use 2 external data sources, a excel dataset from Kaggle and some tsv datasets from IMDb non-com databases.

## **Data Sources:**

- **WoWCinema Platform** – Own platform data, which includes user activity, interactions (likes/dislikes), subscription information and more.
- [**Netflix Movies and TV Shows (Kaggle)**](https://www.kaggle.com/datasets/shivamb/netflix-shows) – Public dataset providing catalog metadata such as title, cast, type, release year, and description.
- [**IMDb Non-Commercial Datasets**](https://developer.imdb.com/non-commercial-datasets/) – Official IMDb non-comercial datasets available, under the IMDb Non-Commercial Data Licens, for personal and academic use; offering structured data on titles, ratings, crew, cast, and more, which will be used only for personal testing.

Note: In accordance with the IMDb Non-Commercial Data License, redistribution of IMDb datasets is not permitted. Therefore, to use the scripts related to IMDb data in the Bronze tier of this project, please create a local folder named IMDb within your project directory and manually place the title.basics.tsv and title.ratings.tsv files there. These files must be downloaded directly from IMDb's official non-commercial dataset page. Thank you for your understanding!

## **Schemas**

- `bronze_wowcinema`

  - Purpose: This schema represents the initial storage for raw, unprocessed data, which is directly extracted from all 3 sources mentioned above.
  - For creating this schema run the following query on your local server: `./bronze/src/schemas/bronze_wowcinema.sql`

- `silver_wowcinema`

  - Purpose: This schema serves to store cleaned and transformed data, ready for further processing down the pipeline.
  - For creating this schema run the following query on your local server: `./bronze/src/schemas/silver_wowcinema.sql`

- `gold_wowcinema`
  - Purpose: this schema serves to store the final, fully processed data that is ready for further analytics and reporting.
  - For creating this schema run the following query on your local server: `./bronze/src/schemas/gold_wowcinema.sql`

## **Bronze Layer**

### **WoWCinema source**

---

`WoWcinema_data`

- A log is considered **“open”** when a user begins watching a title on the platform. It is considered **“closed”** under any of the following conditions:

  - The user leaves the platform before completing the movie.
  - The user finishes watching the movie, scrolls a little bit more afterwards and eventually exits the platform, without starting a new movie/serial.
  - The user finishes the movie and continues browsing, but upon clicking another title, a **new log is created**, and the current one is closed.

- Note: In earlier versions, there was an is_completed column. However, I decided to remove it and instead derive completion status through calculations in later stages of the pipeline (likely during the silver layer transformation).

| Column Name               | Data Type      | Description                                                                            |
| ------------------------- | -------------- | -------------------------------------------------------------------------------------- |
| `log_id`                  | `VARCHAR(50)`  | Unique ID for each activity/session log                                                |
| `username`                | `VARCHAR(100)` | Platform username                                                                      |
| `first_name`              | `VARCHAR(100)` | User’s first name                                                                      |
| `last_name`               | `VARCHAR(100)` | User’s last name                                                                       |
| `birth_date`              | `TIMESTAMP`    | User’s birth date                                                                      |
| `subscription_plan`       | `INT`          | Plan type: 1-Basic/2-Standard/3-Premium                                                |
| `subscription_start_date` | `DATE`         | Start date of the user’s subscription                                                  |
| `iban`                    | `VARCHAR(45)`  | Simulated bank account number                                                          |
| `title_name`              | `VARCHAR(255)` | Watched title name (movie or series)                                                   |
| `watch_start_time`        | `TIMESTAMP`    | When the viewing session started                                                       |
| `watch_end_time`          | `TIMESTAMP`    | When the viewing session ended                                                         |
| `session_duration_min`    | `FLOAT`        | Total session duration in minutes                                                      |
| `rating_given`            | `FLOAT`        | User rating for the title (scale 0–10)                                                 |
| `reaction_type`           | `INT`          | Reaction (1 = like, 0 = neutral, -1 = dislike)                                         |
| `region_code`             | `INT`          | Romania Region (called "judet" in Romanian) code from where the user watched the title |

---

### **Netflix Movies and TV Shows (Kaggle) source**

---

`netflix_kaggle_data`

| Column Name              | Data Type      | Description                                |
| ------------------------ | -------------- | ------------------------------------------ |
| `netf_title`             | `VARCHAR(255)` | title name(title=movie/serial)             |
| `netf_title_type`        | `VARCHAR(10)`  | title category(movie/tv show)              |
| `netf_director`          | `VARCHAR(255)` | Movie Director                             |
| `netf_data_added`        | `VARCHAR(50)`  | Date when movie was uploaded on netflix    |
| `netf_release_year`      | `INT`          | Title release year                         |
| `netf_duration`          | `VARCHAR(15)`  | Unit of measure(movie-min,serials-seasons) |
| `netf_genre`             | `VARCHAR(255)` | Title genre list (minim 1)                 |
| `netf_movie_description` | `text`         | Title description                          |

---

### **IMDb Non-Commercial Datasets source**

---

`IMDb_noncom_basiscs`

| Column Name          | Data Type      | Description                                      | Source File         |
| -------------------- | -------------- | ------------------------------------------------ | ------------------- |
| `imd_tconst `        | `VARCHAR(20)`  | Unique identifier for the title                  | title.basics.tsv.gz |
| `imd_primaryTitle `  | `VARCHAR(255)` | Title name (ex: movie or TV series)              | title.basics.tsv.gz |
| `imd_titleType`      | `VARCHAR(25)`  | Type of title (ex: movie, short, tvSeries, etc.) | title.basics.tsv.gz |
| `startYear`          | `int`          | release year of the title                        | title.basics.tsv.gz |
| `imd_runtimeMinutes` | `VARCHAR(50)`  | Runtime duration ( minutes/seasons)              | title.basics.tsv.gz |
| `imd_genres`         | `text`         | Up to three genres associated with the title     | title.basics.tsv.gz |

`IMDb_noncom_ratings`

| Column Name         | Data Type     | Description                         | Source File          |
| ------------------- | ------------- | ----------------------------------- | -------------------- |
| `imd_tconst `       | `VARCHAR(20)` | Unique identifier for the title     | title.ratings.tsv.gz |
| `imd_averageRating` | `FLOAT`       | Average user rating on IMDb 0-10    | title.ratings.tsv.gz |
| `imd_numVotes`      | `INT`         | Total number of user votes received | title.ratings.tsv.gz |

---

## **Silver Layer**

### `fact_logs`

This is the main table where each row represents a session where a user watched a title.

| Column Name            | Data Type          | Description                                                | Bronze Source                                                                                  |
| ---------------------- | ------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `log_id`               | `VARCHAR(50)` `PK` | Unique ID for each viewing session                         | `bronze/wowcinema_data/log_id`                                                                 |
| `user_id`              | `INT` `FK`         | References the user who watched                            | `dim_users/user_id` — generated and matched based on `username`, `first_name`, and `last_name` |
| `subscription_plan_id` | `INT` `FK`         | References the user's subscription plan                    | `bronze/wowcinema_data/subscription_plan`                                                      |
| `title_id`             | `INT` `FK`         | References the title (movie or show) watched               | `dim_titles/title_id` — generated                                                              |
| `start_time`           | `DATE`             | The date when the session started                          | `bronze/wowcinema_data/watch_start_time` → converted to date                                   |
| `end_time`             | `DATE`             | The date when the session ended                            | `bronze/wowcinema_data/watch_end_time` → converted to date                                     |
| `session_duration`     | `FLOAT`            | How long the session lasted (in minutes)                   | `bronze/wowcinema_data/session_duration_min`                                                   |
| `reaction_id`          | `INT` `FK`         | What the user thought: 1 = like, 0 = neutral, -1 = dislike | `bronze/wowcinema_data/reaction_type` — mapped via `dim_reactions` for flexibility             |
| `rating_given`         | `FLOAT`            | Rating given by the user for that title (0–10 scale)       | `bronze/wowcinema_data/rating_given`                                                           |

---

### `dim_users`

This table contains details about each user who has activity on the platform.

| Column Name               | Data Type      | Description                      | Bronze Source                                   |
| ------------------------- | -------------- | -------------------------------- | ----------------------------------------------- |
| `user_id`                 | `INT` `PK`     | Unique ID for each user          | generated                                       |
| `username`                | `VARCHAR(100)` | The user’s platform username     | `bronze/wowcinema_data/username`                |
| `first_name`              | `VARCHAR(100)` | User’s first name                | `bronze/wowcinema_data/first_name`              |
| `last_name`               | `VARCHAR(100)` | User’s last name                 | `bronze/wowcinema_data/last_name`               |
| `birth_date`              | `DATE`         | User’s birth date                | `bronze/wowcinema_data/birth_date`              |
| `user_iban`               | `VARCHAR(45)`  | Simulated bank account number    | `bronze/wowcinema_data/iban`                    |
| `region_code`             | `INT`          | Region where the user is located | `bronze/wowcinema_data/region_code`             |
| `subscription_start_date` | `TIMESTAMP`    | Subscription start date          | `bronze/wowcinema_data/subscription_start_date` |

---

### `dim_titles`

This table stores information about each title (movie or show) available on the platform.

| Column Name          | Data Type      | Description                                                 | Bronze Source                                                                          |
| -------------------- | -------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `title_id`           | `INT` `PK`     | Unique ID for the title                                     | generated                                                                              |
| `title_name`         | `VARCHAR(255)` | The title’s name                                            | `bronze/netflix_kaggle_data/netf_title`                                                |
| `title_type`         | `VARCHAR(50)`  | Type of content (movie, TV series, etc.)                    | to be completed                                                                        |
| `title_director`     | `VARCHAR(255)` | Director of the title                                       | `bronze/netflix_kaggle_data/netf_director`                                             |
| `title_release_year` | `INT`          | Year when the title was released                            | `bronze/netflix_kaggle_data/netf_release_year`                                         |
| `title_duration`     | `FLOAT`        | Duration of the title in minutes or calculated from seasons | `bronze/netflix_kaggle_data/netf_duration` or `IMDb_noncom_basiscs/imd_runtimeMinutes` |
| `title_genres`       | `VARCHAR(255)` | List of genres (as a raw string, for now)                   | to be completed                                                                        |
| `title_description`  | `TEXT`         | Title description                                           | to be completed                                                                        |

---

### `dim_subscriptions`

This table describes the different types of subscription plans available to users.

| Column Name          | Data Type     | Description                                 |
| -------------------- | ------------- | ------------------------------------------- |
| `subscription_id`    | `INT` `PK`    | Unique ID for the subscription plan         |
| `subscription_plan`  | `VARCHAR(15)` | Name of the plan (Basic, Standard, Premium) |
| `subscription_price` | `FLOAT`       | Monthly price of the subscription           |
| `currency_code`      | `VARCHAR(3)`  | Currency used for pricing (e.g., USD, EUR)  |

---

### `dim_reactions`

This table contains the possible types of user reactions available on the platform.

| Column Name            | Data Type  | Description                                 | Bronze Source                         |
| ---------------------- | ---------- | ------------------------------------------- | ------------------------------------- |
| `reaction_id`          | `INT` `PK` | Unique ID representing the type of reaction | `bronze/wowcinema_data/reaction_type` |
| `reaction_description` | `TEXT`     | Text description for the reaction type      | explained based on `reaction_id`      |
