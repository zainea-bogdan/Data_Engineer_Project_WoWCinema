# Data Warehouse 3 Layers Arhitecture - Bronze-Silver-Gold

> **Note:** The `BSG_arhitecture.drawio` file included in this directory serves primarily as an initial sketch for orientation. It was created early in the design process to visualize the foundational structure of the data warehouse. While it reflects my initial thought process, please be aware that it has not been updated to align with all the refinements and schema evolutions described throughout this documentation.

## Table of Contents

- [Data Sources](#data-sources)
  - [WoWCinema Platform](#wowcinema-platform)
  - [IMDb Non-Commercial Datasets](#imdb-non-commercial-datasets)
- [Schemas](#schemas)
  - [bronze_wowcinema](#bronze_wowcinema)
  - [silver_wowcinema](#silver_wowcinema)
  - [gold_wowcinema](#gold_wowcinema)
- [Bronze Schema Tables Overview](#bronze-schema-tables-overview)
- [Silver Schema Tables Overview](#silver-schema-tables-overview)
- [Gold Schema Tables Overview](#gold-schema-tables-overview)
  - [Design Consideration for the Gold Layer](#design-consideration-for-the-gold-layer)
  - [`cleaned_users_and_subscriptions`](#cleaned_users_and_subscriptions)
  - [`cleaned_titles`](#cleaned_titles)
  - [`cleaned_fact_table`](#cleaned_fact_table)
- [Gold Layer Views](#gold-layer-views)
  - [`movie_completion_ratio_raport`](#movie_completion_ratio_raport)
  - [`average_time_spent_on_platform`](#average_time_spent_on_platform)
  - [`act_inact_user_report`](#act_inact_user_report)
  - [`user_distribution_by_plan`](#user_distribution_by_plan)
  - [`active_and_inactive_users_by_subscription_plan`](#active_and_inactive_users_by_subscription_plan)
  - [`revenue_per_subscription_tier`](#revenue_per_subscription_tier)
  - [`top_10_movie_watched`](#top_10_movie_watched)
  - [`Bottom_10_Least_Watched_Movies`](#bottom_10_least_watched_movies)
  - [`rating_comaprison_plat_imdb`](#rating_comaprison_plat_imdb)

---

## **Data Sources:**

- **WoWCinema Platform** – Own platform data, which includes user activity, interactions (likes/dislikes), subscription information and more.

> From this source, I developed a **log-based session tracking system** designed to simulate user activity on the platform. It operates as follows:
>
> - A log is considered **“open”** when a user begins watching a title.
> - A log is marked as **“closed”** under any of the following conditions:
>   - The user exits the platform
>   - The user begins watching a new title — in this case, the current log is closed and a **new log is created** to capture the subsequent session.

---

- [**IMDb Non-Commercial Datasets**](https://developer.imdb.com/non-commercial-datasets/) – Official IMDb non-comercial datasets available, under the IMDb Non-Commercial Data Licens, for personal and academic use; offering structured data on titles, ratings, crew, cast, and more, which will be used only for personal testing and educational purposes.

> Note: In accordance with the IMDb Non-Commercial Data License, redistribution of IMDb datasets is not permitted. Therefore, to use the scripts related to IMDb data in the Bronze layer of this project, please create a local folder named IMDb within your project directory and manually place the required TSV files there. These files must be downloaded directly from IMDb's official non-commercial dataset page. Thank you for your understanding!

## **Schemas**

- `bronze_wowcinema`

  - **Purpose**: This schema represents the initial storage layer for raw, unprocessed data extracted from multiple source systems.

- `silver_wowcinema`

  - **Purpose**: This schema holds cleaned and semi-structured data, refined for further transformation and business use.

- `gold_wowcinema`

  - **Purpose**: This schema stores the final, fully processed and aggregated data intended for analytics, dashboards, and reporting.

## **Bronze Schema Tables Overview**

| Table Name          | Columns                                                                                                           | Description                                                                                      |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `log_system`        | `id_log`, `id_user`, `titleconst`, `session_start`, `session_end`, `rating_given`, `reaction_type`, `region_code` | Stores platform session logs including user activity, session duration, rating, and region data. |
| `name_basics`       | `nconst`, `primaryname`, `birthyear`, `deathyear`, `knowfortitles`                                                | Contains basic identity information about known individuals (e.g., actors, directors).           |
| `title_ratings`     | `tconst`, `averagerating`, `numvotes`                                                                             | Holds IMDb rating and vote data for each title.                                                  |
| `subscription_plan` | `subscription_plan_id`, `subscription_plan`, `subscription_price`, `currency_code`                                | Defines the subscription plan options available, with prices and currency.                       |
| `title_basics`      | `tconst`, `titletype`, `title`, `isadult`, `startyear`, `runtime`, `genres`                                       | Describes core attributes for all titles (movies/series), including type, runtime, genre, etc.   |
| `title_crew`        | `tconst`, `director`                                                                                              | Stores crew information with references to directing personnel for titles.                       |
| `title_episodes`    | `tconst`, `parenttconst`, `seasonnumber`, `episodenumber`                                                         | Stores episode-level information for series, including season and episode numbers.               |
| `users`             | `id_user`, `first_name`, `last_name`, `birth_date`, `subscription_plan`, `subscription_start_date`, `iban`        | Holds user profile details including name, subscription info, and banking details.               |

---

## Silver Schema Tables Overview

The `silver_wowcinema` schema was designed to organize and optimize the structure of data extracted from the raw **bronze-level source tables**. Based on the cleaned and transformed data, I initially structured it as a **star schema**, with:

- `fact_logs` serving as the central fact table containing user session activity.
- Surrounding `dim_*` tables (e.g., `dim_users`, `dim_titles`, `dim_subscriptions`, `dim_reactions`, and `dim_regions`) acting as descriptive dimensions, each linked via foreign keys.

While originally intended as a traditional star schema for simplified querying and fast aggregation, the schema has gradually **evolved toward a snowflake design**, as some dimensions (e.g., `dim_users` referencing `dim_subscriptions`) began to normalize and reference other dimensions directly.

This refined structure is intended to:

- Improve query performance through clearer relationships and better indexing.
- Support more granular filtering and joins across normalized dimensions.
- Serve as a solid foundation for creating the **gold layer**, where final reporting views and high-level aggregated metrics will be developed.

---

| Table Name          | Columns                                                                                                                                                                    | Description                                                                                             |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `dim_reactions`     | `id_reaction`, `reaction_name`                                                                                                                                             | Lookup table for possible user reactions (e.g., like, neutral, dislike).                                |
| `dim_regions`       | `id_region`, `region_name`                                                                                                                                                 | Contains region identifiers and their associated names.                                                 |
| `dim_subscriptions` | `id_subscription`, `subscription_plan`, `subscription_price`, `currency_code`, `discount_procentual`                                                                       | Defines subscription tiers along with pricing, currency, and discount percentage.                       |
| `dim_titles`        | `id_title`, `title_name`, `title_director_first_name`, `title_director_last_name`, `title_type`, `title_start_year`, `title_duration`, `title_rating`, `title_numvot_imdb` | Stores enriched title-level information used for analytics (fact table reference).                      |
| `dim_users`         | `id_user`, `first_name`, `last_name`, `birth_date`, `id_plan`, `subscription_start_date`, `iban`                                                                           | Contains enriched user profiles linked to subscription plans.                                           |
| `fact_logs`         | `id_log`, `id_user`, `id_title`, `session_start`, `session_end`, `rating_given`, `id_reaction`, `id_region`                                                                | Main fact table storing session logs and linking to all relevant dimensions for reporting and analysis. |

## Gold Schema Tables Overview

### Design Consideration for the Gold Layer

While the `silver_wowcinema` schema was originally modeled as a star schema, it has gradually evolved toward a **snowflake schema**, introducing more normalized relationships between dimension tables. However, in the **gold layer**, the table structure reflects a **simplified version of a real business context**.

To streamline the creation of reporting views and simplify querying logic, I chose to **unify related attributes into wider, denormalized tables** (ex: combining user and subscription details). Although such flattening is not typically recommended for large-scale production environments due to potential redundancy and performance costs, this approach is justified here given the **relatively small data volume** and the **need for simpler, more accessible views** during the reporting phase.

This trade-off prioritizes ease of use and clarity for final analysis over strict normalization.

### `cleaned_users_and_subscriptions`

| Column Name               | Source Table                         | Description                          |
| ------------------------- | ------------------------------------ | ------------------------------------ |
| `id_user`                 | `silver_wowcinema.dim_users`         | Unique ID of the user                |
| `first_name`              | `silver_wowcinema.dim_users`         | User's first name                    |
| `last_name`               | `silver_wowcinema.dim_users`         | User's last name                     |
| `birth_date`              | `silver_wowcinema.dim_users`         | User's date of birth                 |
| `iban`                    | `silver_wowcinema.dim_users`         | User's simulated bank account number |
| `id_plan`                 | `silver_wowcinema.dim_users`         | ID of the user’s subscription plan   |
| `subscription_start_date` | `silver_wowcinema.dim_users`         | Start date of the subscription       |
| `subscription_plan`       | `silver_wowcinema.dim_subscriptions` | Name of the subscription plan        |
| `subscription_price`      | `silver_wowcinema.dim_subscriptions` | Price of the subscription plan       |
| `currency_code`           | `silver_wowcinema.dim_subscriptions` | Currency used for the subscription   |
| `discount_procentual`     | `silver_wowcinema.dim_subscriptions` | Discount percentage on the plan      |

---

### `cleaned_titles`

| Column Name                 | Source Table                  | Description                      |
| --------------------------- | ----------------------------- | -------------------------------- |
| `id_title`                  | `silver_wowcinema.dim_titles` | Title unique identifier          |
| `title_name`                | `silver_wowcinema.dim_titles` | Title name (movie or series)     |
| `title_director_first_name` | `silver_wowcinema.dim_titles` | Director's first name            |
| `title_director_last_name`  | `silver_wowcinema.dim_titles` | Director's last name             |
| `title_type`                | `silver_wowcinema.dim_titles` | Type of title (e.g. movie, show) |
| `title_start_year`          | `silver_wowcinema.dim_titles` | Release year                     |
| `title_duration`            | `silver_wowcinema.dim_titles` | Runtime in minutes               |
| `title_rating`              | `silver_wowcinema.dim_titles` | Average rating                   |
| `title_numvot_imdb`         | `silver_wowcinema.dim_titles` | Number of votes on IMDb          |

---

### `cleaned_fact_table`

| Column Name     | Source Table                   | Description                                     |
| --------------- | ------------------------------ | ----------------------------------------------- |
| `id_log`        | `silver_wowcinema.fact_logs`   | Unique session log ID                           |
| `id_user`       | `silver_wowcinema.fact_logs`   | Foreign key referencing the user                |
| `id_title`      | `silver_wowcinema.fact_logs`   | Foreign key referencing the watched title       |
| `session_start` | `silver_wowcinema.fact_logs`   | Timestamp for when the session started          |
| `session_end`   | `silver_wowcinema.fact_logs`   | Timestamp for when the session ended            |
| `rating_given`  | `silver_wowcinema.fact_logs`   | Rating the user gave                            |
| `id_reaction`   | `silver_wowcinema.fact_logs`   | ID representing a like/dislike/neutral reaction |
| `id_region`     | `silver_wowcinema.fact_logs`   | Region ID where the session took place          |
| `region_name`   | `silver_wowcinema.dim_regions` | Human-readable name of the region               |

## Gold Layer Views

The entire gold layer table structure was designed with a clear objective: to enable efficient, accurate, and simplified reporting for business insights. After progressively modeling and refining data from raw extraction to structured entities, this unified and analytics-ready layer supports the creation of the following views. Each view serves as a strategic output of the warehouse architecture, centralizing metrics required by the **Business Requirements** for dashboards, monitoring, and decision-making.

Below are the resulting views, each tailored to address a specific business question or reporting need, providing direct access to consolidated and actionable insights derived from the underlying gold-layer tables.

---

### `movie_completion_ratio_raport`

- **Purpose:** Computes the average movie completion rate by comparing session time with movie duration.
- **Business Requirement Report:** Movie Completion Report
- **Source Tables:**
  - `gold_wowcinema.cleaned_fact_table` — provides session start/end and user activity
  - `gold_wowcinema.cleaned_titles` — provides movie duration (`title_duration`)

---

### `average_time_spent_on_platform`

- **Purpose:** Calculates the average duration of viewing sessions across users.
- **Business Requirement Report:** Session Duration Report
- **Source Tables:**
  - `gold_wowcinema.cleaned_fact_table` — provides timestamps for session start/end
  - `gold_wowcinema.cleaned_titles` — used for fallback logic if duration is unavailable

---

### `act_inact_user_report`

- **Purpose:** Classifies users as active or inactive based on their number of interactions.
- **Business Requirement Report:** Active vs. Inactive User Report
- **Source Tables:**
  - `gold_wowcinema.cleaned_fact_table` — logs representing user activity
  - `gold_wowcinema.cleaned_users_and_subscriptions` — all registered users

---

### `user_distribution_by_plan`

- **Purpose:** Shows the number of users per subscription plan.
- **Business Requirement Report:** User Distribution Across Subscription Plans
- **Source Tables:**
  - `gold_wowcinema.cleaned_users_and_subscriptions` — user data with plan assignment

---

### `active_and_inactive_users_by_subscription_plan`

- **Purpose:** Groups active/inactive users by the subscription plan they belong to.
- **Business Requirement Report:** Active vs. Inactive Users by Subscription Plan
- **Source Tables:**
  - `gold_wowcinema.cleaned_fact_table` — log entries used to determine activity
  - `gold_wowcinema.cleaned_users_and_subscriptions` — user and subscription data

---

### `revenue_per_subscription_tier`

- **Purpose:** Computes the revenue generated per subscription tier by multiplying user count with plan price.
- **Business Requirement Report:** Revenue Analysis by Subscription Tier
- **Source Tables:**
  - `gold_wowcinema.cleaned_users_and_subscriptions` — contains subscription tier and pricing info

---

### `top_10_movie_watched`

- **Purpose:** Lists the top 10 movies with the highest number of views/interactions.
- **Business Requirement Report:** Top 10 Most Watched Movies
- **Source Tables:**
  - `gold_wowcinema.cleaned_fact_table` — session logs used to count views
  - `gold_wowcinema.cleaned_titles` — movie details

---

### `Bottom_10_Least_Watched_Movies`

- **Purpose:** Lists the 10 least viewed movies based on number of sessions logged.
- **Business Requirement Report:** Bottom 10 Least Watched Movies
- **Source Tables:**
  - `gold_wowcinema.cleaned_fact_table` — log activity for view count
  - `gold_wowcinema.cleaned_titles` — metadata for movies

---

### `rating_comaprison_plat_imdb`

- **Purpose:** Compares the average user rating on the WoWCinema platform to IMDb's average rating.
- **Business Requirement Report:** Platform vs. IMDb Rating Comparison
- **Source Tables:**
  - `gold_wowcinema.cleaned_fact_table` — user ratings (`rating_given`)
  - `gold_wowcinema.cleaned_titles` — IMDb average ratings (`title_rating`)
