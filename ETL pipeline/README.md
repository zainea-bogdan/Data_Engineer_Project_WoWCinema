# ETL pipeline

- Extract

  - Scope: This process is performed at the bronze tier level (on raw data), where data is ingested and loaded into raw staging tables without transformations.

- Transform

  - Scope: This process is performed at the silver tier level (on partially cleaned data), where the raw data is cleaned, standardized, and structured into logically related tables.

- Load
  - Scope: This process is performed at the gold tier level, where final views and business-ready tables are created to support the core business goals, reports, dashboards, and KPIs.
