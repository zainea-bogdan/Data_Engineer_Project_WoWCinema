# Data_Engineer_Project_WoWCinema

## Fictive Scenario

You are a Data Engineer in the WoWCinema company. The WoWCinema company is a Romanian StartUp in movie streaming industry and offers details about a large variety of films for their customers, and also provide the films as well.

### Core Business Goals

---

1. **Movie Completion Analytics** – Track how often users complete movies and what influences completion rate.
2. **Churn Prediction & Retention** – Identify inactive or disengaged users and drive proactive retention.
3. **Genre Popularity by Region** – Analyze movie genre trends across different countries.
4. **Subscription Plan Optimization** – Evaluate which subscription tiers perform best based on user activity and duration.

#### Reports

---

- **Completion rate per movie**
- **Top 10 genres by total watch time**
- **User churn risk list** (inactive or low engagement users)
- **Average session duration by subscription plan**

#### Dashboards

---

- **Top 10 completed movies** (monthly)
- **Most trending genres by country** (heatmap)
- **New subscribers vs churned users** (monthly growth)
- **Estimated monthly revenue by subscription plan**

#### KPIs

---

- **Average movie completion rate**
  - Formula: total completed sessions ÷ total sessions
- **Monthly active users**
  - Unique users engaging per month
- **Churn rate**
  - Formula: users inactive >30 days ÷ total active users
- **Genre watch share**
  - Formula: genre watch time ÷ total watch time
- **Top subscription plan by revenue**
  - Plan revenue = plan price × number of users

## Data Warehouse Design

It has a server `WoWCinema` and a database named `WoWCinema`.

### Sources

The data sources for the company are:

- **WoWCinema Platform** – Own platform data, which includes user activity, interactions (likes/dislikes), and subscription information.
- [**Netflix Movies and TV Shows (Kaggle)**](https://www.kaggle.com/datasets/shivamb/netflix-shows) – Public dataset providing catalog metadata such as title, cast, type, release year, and description.
- [**IMDb Non-Commercial Datasets**](https://developer.imdb.com/non-commercial-datasets/) – Official IMDb datasets available for personal and academic use, offering structured data on titles, ratings, crew, cast, and more.

#### **WoWCinema source**

`WoWcinema_data`

- A log is considered **“open”** when a user begins watching a title on the platform. It is considered **“closed”** under any of the following conditions:

  - The user leaves the platform before completing the movie.
  - The user finishes watching the movie, scrolls a little bit more afterwards and eventually exits the platform, without starting a new movie/serial.
  - The user finishes the movie and continues browsing, but upon clicking another title, a **new log is created**, and the current one is closed.

- Note: In earlier versions, there was an is_completed column. However, I decided to remove it and instead derive completion status through calculations in later stages of the pipeline (likely during the silver layer transformation).

| Column Name               | Data Type      | Description                                        |
| ------------------------- | -------------- | -------------------------------------------------- |
| `log_id`                  | `VARCHAR(50)`  | Unique ID for each activity/session log            |
| `username`                | `VARCHAR(100)` | Platform username                                  |
| `first_name`              | `VARCHAR(100)` | User’s first name                                  |
| `last_name`               | `VARCHAR(100)` | User’s last name                                   |
| `subscription_status`     | `INT`          | Subscription status (Active/Inactive - 1/0)        |
| `subscription_plan`       | `INT`          | Plan type: 1-Basic/2-Standard/3-Premium            |
| `subscription_start_date` | `DATE`         | Start date of the user’s subscription              |
| `iban`                    | `VARCHAR(45)`  | Simulated bank account number                      |
| `title_name`              | `VARCHAR(255)` | Watched title name (movie or series)               |
| `watch_start_time`        | `TIMESTAMP`    | When the viewing session started                   |
| `watch_end_time`          | `TIMESTAMP`    | When the viewing session ended                     |
| `session_duration_min`    | `FLOAT`        | Total session duration in minutes                  |
| `rating_given`            | `FLOAT`        | User rating for the title (scale 0–10)             |
| `reaction_type`           | `INT`          | Reaction (1 = like, 0 = neutral, -1 = dislike)     |
| `country_code`            | `VARCHAR(70)`  | Country code from where the user watched the title |

#### **Netflix Movies and TV Shows (Kaggle) source**

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

#### **IMDb Non-Commercial Datasets source**

`IMDb_noncom_data`

| Column Name          | Data Type      | Description                                      | Source File          |
| -------------------- | -------------- | ------------------------------------------------ | -------------------- |
| `imd_titleId`        | `VARCHAR(500)` | Unique identifier for the title                  | title.akas.tsv.gz    |
| `imd_title`          | `VARCHAR(255)` | Title name (ex: movie or TV series)              | title.akas.tsv.gz    |
| `imd_titleType`      | `VARCHAR(50)`  | Type of title (ex: movie, short, tvSeries, etc.) | title.basics.tsv.gz  |
| `imd_runtimeMinutes` | `VARCHAR(50)`  | Runtime duration ( minutes/seasons)              | title.basics.tsv.gz  |
| `imd_genres`         | `VARCHAR(500)` | Up to three genres associated with the title     | title.basics.tsv.gz  |
| `imd_averageRating`  | `FLOAT`        | Average user rating on IMDb 0-10                 | title.ratings.tsv.gz |
| `imd_numVotes`       | `INT`          | Total number of user votes received              | title.ratings.tsv.gz |
