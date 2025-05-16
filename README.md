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

---

The data sources for the company are:

- **WoWCinema Platform** – Own platform data, which includes user activity, interactions (likes/dislikes), and subscription information.
- [**Netflix Movies and TV Shows (Kaggle)**](https://www.kaggle.com/datasets/shivamb/netflix-shows) – Public dataset providing catalog metadata such as title, cast, type, release year, and description.
- [**IMDb Non-Commercial Datasets**](https://developer.imdb.com/non-commercial-datasets/) – Official IMDb datasets available for personal and academic use, offering structured data on titles, ratings, crew, cast, and more.

PS: For each source listed above, i have created a specific table in the bronze stage, more details in [bronze stage README.md](./bronze/README.md)

### Schemas

---

- **bronze_wowschema**
  - Purpose: This schema represents the initial storage for raw, unprocessed data, which is directly extracted from all 3 sources mentioned above.
- **silver_wowcinema**
  - Purpose: This schema serves to store cleaned and transformed data, ready for further processing down the pipeline.
- **gold_wowschema**
  - Purpose: this schema serves to store the final, fully processed data that is ready for further analytics and reporting.

### ETL pipeline

---

- [Extract](./bronze/src/extract/)

  - Scope: This process is performed at the bronze tier level (on raw data), where data is ingested and loaded into raw staging tables without transformations.

- Transform

  - Scope: This process is performed at the silver tier level (on partially cleaned data), where the raw data is cleaned, standardized, and structured into logically related tables.

- Load
  - Scope: This process is performed at the gold tier level, where final views and business-ready tables are created to support the core business goals, reports, dashboards, and KPIs.
