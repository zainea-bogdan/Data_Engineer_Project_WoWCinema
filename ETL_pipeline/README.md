# ETL Pipeline - Step by Step

> **Note 1:** Due to a lack of attention to detail during the initial planning phase, a separate table for platform-specific titles was not created. To compensate for this, I simulated the missing `title` dataset by selecting the top 15,000 titles from the IMDb dataset using a custom filtering process in Pandas. This subset was used to approximate the platform's catalog and support downstream analytical needs. Given the large size of the original IMDb datasets, not all available data was ingested—this was an intentional decision to allow for faster prototyping and development cycles. Consequently, some data cleaning operations that were initially intended for the Silver layer were performed earlier in the Bronze layer to align with the filtered extraction. While some Python scripts used in this phase may not yet be fully optimized, the project will continue to evolve, and code quality will be incrementally improved in future updates.

> **Note 2:** At the current stage, the entire ETL process — from schema creation to data ingestion, transformation, and reporting view generation — is performed manually. This approach was intentional, aiming to provide full transparency into each step. It facilitates better understanding of the underlying logic, supports easier troubleshooting, and encourages suggestions for optimization and future project evolution.

## Extract Phase

The **Extract** phase is the first step in the ETL (Extract, Transform, Load) process and plays a critical role in data warehousing. Its purpose is to collect raw data from various structured and semi-structured sources—both internal and external—and prepare it for downstream processing. In the context of this project, the extract step involves sourcing data from IMDb datasets and platform-generated activity, which is then stored in the Bronze layer as-is, with minimal transformation.

The `extract` folder under `ETL_pipeline/src/` contains all scripts responsible for extracting data and populating the Bronze schema with initial raw records. These scripts should be executed in a specific order to ensure correct schema setup and data integrity.

### Script Execution Order and Purpose

1. **`bronze_layer_structure.py`**

   - Initializes the `bronze_wowcinema` schema by creating all required tables.
   - This script must be run **first**, as it sets up the database structure for subsequent inserts.

2. **IMDb Data Extraction**

   - These scripts load structured metadata from IMDb TSV files into the corresponding Bronze tables:
     - `extract_title_basics.py`
     - `extract_title_crew.py`
     - `extract_title_episodes.py`
     - `extract_title_ratings.py`
     - `extract_director_name.py`
   - The TSV files must be downloaded manually and placed in a local `IMDb/` directory before running these scripts.

3. **Platform User & Subscription Data**

   - These scripts simulate platform-specific entities:
     - `extract_users.py` – creates user profiles with personal and subscription details.
     - `extract_subscriptions.py` – defines available subscription plans and pricing tiers.

4. **Log System Simulation**
   - `extract_logs.py` generates synthetic user activity logs that simulate session behavior on the platform.
   - This log system is key to enabling downstream engagement and usage analytics.

## Transform Phase

The **Transform** phase is responsible for converting the raw records from the Bronze layer into a structured and normalized format suitable for analytics. This is where the Silver layer is built—organizing the data into fact and dimension tables while applying key cleaning and transformation logic.

The transformation scripts are located in: `ETL_pipeline/src/transform/`

### Script Execution Order and Purpose

1. **`creating_silver_layer.py`**

   - This is the primary script for building the `silver_wowcinema` schema.
   - It transforms and distributes the Bronze data into properly normalized tables, including:
     - `fact_logs`
     - `dim_users`
     - `dim_titles`
     - `dim_subscriptions`
     - `dim_reactions`
     - `dim_regions`
   - It includes logic for key management, enrichment, and value alignment needed before loading into the Gold layer.

2. **`dim_region.py`** _(optional)_
   - An auxiliary script used during early development for handling region data separately.
   - This is not required for final execution if `creating_silver_layer.py` is used.

> For standard execution, **only** `creating_silver_layer.py` needs to be run to fully create and populate the Silver schema.

## Load Layer

The **Load** phase represents the final step in the ETL pipeline. Its purpose is to consolidate and load the transformed data from the Silver layer into the **Gold layer**, where it is aggregated, cleaned, and optimized for reporting, dashboarding, and analytics.

The load scripts are located in:`ETL_pipeline/src/load/`

### Script Execution Order and Purpose

1. **`loader.py`**
   - This is the only script required for the Load phase.
   - It performs two key functions:
     - **Creates the final Gold-layer tables**, including denormalized structures for users, titles, and activity logs.
     - **Generates the views** that address the business reporting requirements, making the data consumable for stakeholders and analysts.
   - This script bridges the transformation output from Silver and delivers curated, analysis-ready datasets.

> Run only `loader.py` to build the full Gold schema and associated reporting views. No additional scripts are needed in this phase.
