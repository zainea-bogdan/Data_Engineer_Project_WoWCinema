# Silver Stage

## Schema:

- silver_wowcinema

## Table structure:

### `fact_log`

This is the main table where each row represents a session where a user watched a title. It holds info like session duration, rating, and reactions.

| Column Name      | Data Type   | Description                                                | Bronze Source                                        |
| ---------------- | ----------- | ---------------------------------------------------------- | ---------------------------------------------------- |
| log_id           | VARCHAR(50) | Unique ID for each viewing session                         | bronze/wowcinema_data/log_id                         |
| user_id          | INT         | References the user who watched                            | dim_user/id_user ->generated                         |
| title_id         | INT         | References the title (movie or show) watched               | silver/dim_title/id_title                            |
| subscription_id  | INT         | References the user's subscription plan                    | bronze/wowcinema_data/susbscription_plan             |
| watch_date       | DATE        | The date when the session started                          | bronze/wowcinema/watch_start_time->converted to date |
| session_duration | FLOAT       | How long the session lasted (in minutes)                   | bronze/wowcinema_data/session_duration_min           |
| rating_given     | FLOAT       | Rating given by the user for that title (0–10 scale)       | bronze/wowcinema_data/reaction/type                  |
| reaction_id      | INT         | What the user thought: 1 = like, 0 = neutral, -1 = dislike | bronze/wowcinema_data/reaction-type                  |

---

### `dim_user`

This table contains details about each user who has activity on the platform.

| Column Name     | Data Type    | Description                           | Bronze Source                            |
| --------------- | ------------ | ------------------------------------- | ---------------------------------------- |
| user_id         | INT          | Unique ID for each user               | generated                                |
| username        | VARCHAR(100) | The user’s platform username          | bronze/wowcinema_data/username           |
| first_name      | VARCHAR(100) | User’s first name                     | bronze/wowcinema_data/first_name         |
| last_name       | VARCHAR(100) | User’s last name                      | bronze/wowcinema_data/last_name          |
| country_code    | VARCHAR(70)  | Country where the user is located     | bronze/wowcinema_data/country_code       |
| subscription_id | INT          | ID of the subscription the user is on | bronze/wowcinema_data/ subscription_plan |

---

### `dim_title`

This table stores information about each title (movie or show) available on the platform.

| Column Name     | Data Type    | Description                               | Bronze Source                                |
| --------------- | ------------ | ----------------------------------------- | -------------------------------------------- |
| title_id        | INT          | Unique ID for the title                   | generated                                    |
| title_name      | VARCHAR(255) | The title’s name                          | bronze/netflix_kaggle_data/netf_title        |
| release_year    | INT          | Year when the title was released          | bronze/netflix_kaggle_data/netf_release_year |
| title_type      | VARCHAR(50)  | Type of content (movie, TV series, etc.)  | to be completed                              |
| runtime_minutes | FLOAT        | Duration of the title in minutes          | bronze/netflix_kaggle_data/netf_duration     |
| title_genres    | VARCHAR(255) | List of genres (as a raw string, for now) | to be completed                              |

---

### `dim_subscription`

This table describes the different types of subscription plans available to users.

| Column Name | Data Type | Description | Bronze Source |
| ------------------ | ----------- | ------------------------------------------- | ------------- | bronze/subscription_plan/
| subscription_id | INT | Unique ID for the subscription plan |bronze/subscription_plan/subscription_plan_id |
| subscription_plan | VARCHAR(15) | Name of the plan (Basic, Standard, Premium) | bronze/subscription_plan/subscription_plan|
| subscription_price | FLOAT | Monthly price of the subscription |bronze/subscription_plan/subscription_price |
| currency_code | VARCHAR(3) | Currency used for pricing (e.g., USD, EUR) |bronze/subscription_plan/currency_code |

### `dim_reaction`

This table contains the possible types of user reactions available on the platform.

| Column Name   | Data Type   | Description                                 | Bronze Source                        |
| ------------- | ----------- | ------------------------------------------- | ------------------------------------ |
| reaction_id   | INT         | Unique ID representing the type of reaction | bronze/wowcinema_data/reaction_type  |
| reaction_name | VARCHAR(20) | Text label for the reaction type            | explained at reaction_id in fact log |
