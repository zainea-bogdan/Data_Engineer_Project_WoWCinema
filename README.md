# First_Data_Engineer_Personal_Project

## Fictive Scenario

You are a Data Engineer in the WoWCinema company. The WoWCinema company is a Romanian StartUp in movie streaming industry and offers details about a large variety of films for their customers, and also provide the films as well.

### Core Business Goals

---

1. **Movie details** - Aggregate movie-related data and content details.
2. **Movies insights** - Track trends in movie popularity based on rating and viewers feedback.
3. **Popularity trends** - Provide benchmarks and comparisons for different movies, from different platforms.
4. **Movie ranking** - Determine which movies are most popular, using available metrics.

#### Reports

---

- **Numbers of likes** per movie
- **Numbers of dislikes** per movie
- **Top 10 movies** by user rating
- **Least 10 movies** by user rating
- **Number of users** by subscription plan

#### Dashboards

---

- **Top 10 movies** by number of likes(monthly)
- **Number of new users** (monthly)
- **Estimated income** by the end of the month
- **Daily average of active users** for each month

#### KPIs

---

- Total number of active users (measures how many users engaged with the platform in a given period)
- Monthly user growth rate (measures how fast the user base is increasing month over month)
- Top subscription plan by user count ( identifies the most popular plan (ex: Basic, Standard, Premium)).

## Data Warehouse Design

It has a server `WoWCinema` and a database named `WoWCinema`.

### Sources

The data sources for the company are:

- **WoWCinema Platform** – Own platform data, which includes user activity, interactions (likes/dislikes), and subscription information.
- [**Netflix Movies and TV Shows (Kaggle)**](https://www.kaggle.com/datasets/shivamb/netflix-shows) – Public dataset providing catalog metadata such as title, cast, type, release year, and description.
- [**IMDb Non-Commercial Datasets**](https://developer.imdb.com/non-commercial-datasets/) – Official IMDb datasets available for personal and academic use, offering structured data on titles, ratings, crew, cast, and more.

#### **WoWCinema source**

`WoWcinema_data`

| Column Name               | Data Type      | Description                                      |
| ------------------------- | -------------- | ------------------------------------------------ |
| `log_id`                  | `VARCHAR(50)`  | Unique ID for each activity/session log          |
| `user_id`                 | `VARCHAR(20)`  | Unique identifier for each user                  |
| `username`                | `VARCHAR(50)`  | Platform username                                |
| `first_name`              | `VARCHAR(100)` | User’s first name                                |
| `last_name`               | `VARCHAR(100)` | User’s last name                                 |
| `status_subscription`     | `VARCHAR(10)`  | User subscription status (Active/Inactive)       |
| `subscription_plan`       | `VARCHAR(20)`  | Plan type (Basic,Standard,Premium)               |
| `subscription_start_date` | `DATE`         | Start date of the current subscription           |
| `iban`                    | `VARCHAR(45)`  | Simulated bank account number                    |
| `title_name`              | `VARCHAR(255)` | Movie/Serial name                                |
| `watch_timestamp`         | `TIMESTAMP`    | how long did user watched of a specific title    |
| `is_completed`            | `INT`          | Whether the movie was fully watched (1-yes/0-no) |
| `rating_given`            | `FLOAT`        | User rating (0-10)                               |
| `react_type`              | `INT`          | Reaction type (like/nothing/dislike(1/0/-1))     |
| `country`                 | `VARCHAR(70)`  | Country where the session took place             |
| `end_session`             | `Timestamp`    | End time of the viewing session                  |

#### **Netflix Movies and TV Shows (Kaggle) source**

`netflix_kaggle_data`

| Column Name              | Data Type       | Description                                |
| ------------------------ | --------------- | ------------------------------------------ |
| `netf_title`             | `VARCHAR(255)`  | title name(title=movie/serial)             |
| `netf_director`          | `VARCHAR(255)`  | Movie Director                             |
| `netf_data_added`        | `VARCHAR(50)`   | Date when movie was uploaded on netflix    |
| `netf_duration`          | `VARCHAR(15)`   | Unit of measure(movie-min,serials-seasons) |
| `netf_genre`             | `VARCHAR(255)`  | Title genre                                |
| `netf_movie_description` | `VARCHAR(1000)` | Title description                          |

#### **IMDb Non-Commercial Datasets source**

`IMDb_noncom_data`

| Column Name          | Data Type      | Description                                      | Source File          |
| -------------------- | -------------- | ------------------------------------------------ | -------------------- |
| `idm_titleId`        | `VARCHAR(500)` | Unique identifier for the title                  | title.akas.tsv.gz    |
| `idm_title`          | `VARCHAR(255)` | Title name (ex: movie or TV series)              | title.akas.tsv.gz    |
| `idm_titleType`      | `VARCHAR(50)`  | Type of title (ex: movie, short, tvSeries, etc.) | title.basics.tsv.gz  |
| `idm_runtimeMinutes` | `VARCHAR(50)`  | Runtime duration ( minutes/seasons)              | title.basics.tsv.gz  |
| `idm_genres`         | `VARCHAR(500)` | Up to three genres associated with the title     | title.basics.tsv.gz  |
| `idm_averageRating`  | `FLOAT`        | Average user rating on IMDb 0-10                 | title.ratings.tsv.gz |
| `idm_numVotes`       | `INT`          | Total number of user votes received              | title.ratings.tsv.gz |
