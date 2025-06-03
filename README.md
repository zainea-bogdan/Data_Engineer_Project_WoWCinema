# **WoWCinema Data Project**

Welcome to my first end-to-end data project — **WoWCinema Repository**. This project is inspired by the [InternIT Repository](https://github.com/romanmurzac/InternIT/tree/main), and serves as a comprehensive record of my learning journey across multiple areas of the data field. It combines both theoretical concepts and practical implementations, with the primary objective of simulating a real-world business environment by designing and implementing a complete data solution, from ingestion and transformation to analytics and visualization, using industry-relevant tools and best practices.

## Tech Stack

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

## **Project's Purpose:**

As mentioned earlier, this repository is intended to document my journey of learning and applying Big Data concepts. It is structured in a logical manner that reflects my personal approach to learning, emphasizing how I apply theoretical knowledge to my project-based scenario.

Through this project, _my objectives_ are to:

- Build a solid understanding of core Big Data concepts and modern data workflows.
- Simulate a real business context to define meaningful requirements and goals
- Improve my ability to structure work, track progress, and document the development process.
- Gain practical experience with widely used tools and technologies across the data stack.(ex: PostgreSQL,Python, PowerBi)

Ultimately, this project aims to help me develop both breadth and depth across the Big Data field, preparing me for possible future roles,primarily focusing on: Data Engineer, Data Analyst,Database Administrator and Data Warehouse Arhitect.

## **Business Context**

I am a **Data Engineer** at **WoWCinema**, a young, ambitious Romanian startup in the online movie streaming industry. WoWCinema's mission is to make international film content easily accessible to Romanian audiences, with a long-term vision of promoting Romanian cinema as well and expanding throughout Eastern Europe.

WoWcinema's platform offers a diverse catalog of the latest global releases, and they are actively working to integrate Romanian titles as part of their identity. Users can choose from three flexible subscription plans, tailored to various budgets. They also provide movie recommendations based on user behavior and preferences, along with personalized dashboards and viewer engagement analytics.

To succeed in a competitive market, WoWCinema relies on data to guide user engagement, retention, and content acquisition strategies.

As the **Data Engineer** of WoWCinema, I am responsible for designing, building, and maintaining the data infrastructure that powers the company's reporting, analytics, and internal decision-making systems. My objective is to ensure that data is:

- **Precisely collected** from the right sources (ex: external databases, internal systems)
- **Securely stored** in a well-structured and scalable data warehouse.
- **Efficiently processed** through a robust ETL pipeline.
- **Governed and compliant** with applicable data privacy regulations, such as GDPR.
- **Analytics-ready**, enabling data analysts and business stakeholders to measure company performance and make informed, data-driven decisions.

For more details on core business goals, required [reports](./Business_Requirements/README.md#Reports), desired [dashboards](./Business_Requirements/README.md#Dashboards), and key performance indicators ([KPIs](./Business_Requirements/README.md#KPIs)), please refer to the folder named: [Business Requirements](./Business_Requirements/README.md).

## Table of Contents

- [Business_Requirements](./Business_Requirements/)
- [Dashboards_Power_BI](./Dashboards_Power_BI/)
- [Data_Warehouse_Arhitecture](./Data_Warehouse_Arhitecture/)
  - [src](./Data_Warehouse_Arhitecture/src/)
    - [bronze](./Data_Warehouse_Arhitecture/src/bronze/)
      - [creating](./Data_Warehouse_Arhitecture/src/bronze/creating/)
      - [inserting](./Data_Warehouse_Arhitecture/src/bronze/inserting/)
      - [selecting](./Data_Warehouse_Arhitecture/src/bronze/selecting/)
      - [sequences](./Data_Warehouse_Arhitecture/src/bronze/sequences/)
    - [gold](./Data_Warehouse_Arhitecture/src/gold/)
      - [creating](./Data_Warehouse_Arhitecture/src/gold/creating/)
    - [schemas](./Data_Warehouse_Arhitecture/src/schemas/)
    - [silver](./Data_Warehouse_Arhitecture/src/silver/)
      - [creating](./Data_Warehouse_Arhitecture/src/silver/creating/)
      - [inserting](./Data_Warehouse_Arhitecture/src/silver/inserting/)
- [ETL_pipeline](./ETL_pipeline/)
  - [src](./ETL_pipeline/src/)
    - [extract](./ETL_pipeline/src/extract/)
    - [load](./ETL_pipeline/src/load/)
    - [transform](./ETL_pipeline/src/transform/)
- [IMDb](./IMDb/)

## Repository tree:

- The structure of the repository is outlined below. Each main folder includes:
  - A **`README.md`** file, which provides detailed explanations of the folder's contents along with instructions for practical tasks.
  - A **`src/`** subfolder, which contains the source code relevant to that specific component.

```
+---Business_Requirements
|       README.md
|
+---Dashboards_Power_BI
+---Data_Warehouse_Arhitecture
|   |   BSG_arhitecture.drawio
|   |   README.md
|   |
|   \---src
|       +---bronze
|       |   +---creating
|       |   |       create_table_logs_system.sql
|       |   |       create_table_name_basics.sql
|       |   |       create_table_ratings.sql
|       |   |       create_table_subscription_plans.sql
|       |   |       create_table_title_basics.sql
|       |   |       create_table_title_crew.sql
|       |   |       create_table_title_episodes.sql
|       |   |       create_table_users.sql
|       |   |
|       |   +---inserting
|       |   |       insert_logs.sql
|       |   |       insert_subscriptions.sql
|       |   |       insert_title_basics.sql
|       |   |       insert_title_directors.sql
|       |   |       insert_title_director_names.sql
|       |   |       insert_title_episodes.sql
|       |   |       insert_title_ratings.sql
|       |   |       insert_users.sql
|       |   |
|       |   +---selecting
|       |   |       select_all_directors_codes_from_crew.sql
|       |   |       select_all_users.sql
|       |   |       select_id_users.sql
|       |   |       select_subscription_start_date.sql
|       |   |       select_tconst_basics.sql
|       |   |
|       |   \---sequences
|       |           logs_counter.sql
|       |           user_counter.sql
|       |
|       +---gold
|       |   +---creating
|       |   |       creating_gold_layer_structure_and_data.sql
|       |   |       creating_views_for_reports.sql
|       |   |
|       |   +---inserting
|       |   \---selecting
|       +---schemas
|       |       create_bronze_schema.sql
|       |       create_gold_schema.sql
|       |       create_silver_schema.sql
|       |
|       \---silver
|           +---creating
|           |       create_dim_reactions.sql
|           |       create_dim_regions.sql
|           |       create_dim_subscriptions.sql
|           |       create_dim_titles.sql
|           |       create_dim_users.sql
|           |       create_table_fact_logs.sql
|           |       judete_romania.txt
|           |
|           +---inserting
|           |       insert_dim_reactions.sql
|           |       insert_dim_regions.sql
|           |       insert_dim_subscriptions.sql
|           |       insert_dim_titles.sql
|           |       insert_dim_users.sql
|           |       insert_fact_logs.sql
|           |
|           \---selecting
+---ETL_pipeline
|   \---src
|       |   README.md
|       |
|       +---extract
|       |       bronze_layer_structure.py
|       |       extract_director_name.py
|       |       extract_logs.py
|       |       extract_subscriptions.py
|       |       extract_title_basics.py
|       |       extract_title_crew.py
|       |       extract_title_episodes.py
|       |       extract_title_ratings.py
|       |       extract_users.py
|       |
|       +---load
|       |       loader.py
|       |
|       \---transform
|               creating_silver_layer.py
|               dim_region.py
|
\---IMDb
```
