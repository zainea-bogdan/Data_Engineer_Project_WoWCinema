# WoWCinema Data Project

Welcome to my first end-to-end data project — **WoWCinema Repository**. This project is inspired by the [InternIT Repository](https://github.com/romanmurzac/InternIT/tree/main), and serves as a comprehensive record of my learning journey across multiple areas of the data field. It combines both theoretical concepts and practical implementations, with the primary objective of simulating a real-world business environment by designing and implementing a complete data solution — from ingestion and transformation to analytics and visualization — using industry-relevant tools and best practices.

## Purpose:

As mentioned earlier, this repository is intended to document my journey of learning and applying Big Data concepts. It is structured in a logical manner that reflects my personal approach to learning — emphasizing how I apply theoretical knowledge to practical, project-based scenarios.

Through this project, my objectives are to:

- Build a solid understanding of core Big Data concepts and modern data workflows
- Simulate a real business context to define meaningful requirements and goals
- Improve my ability to structure work, track progress, and document the development process
- Gain practical experience with widely used tools and technologies across the data stack
- Explore different areas of the data profession to better understand where my strengths and interests align

Ultimately, this project aims to help me develop both breadth and depth across the Data field, prepari++ng me for possible future roles — primarily in data engineering, but also exploring database administration, analytics, and other related data disciplines.

## Fictive Scenario

I am a **Data Engineer at WoWCinema**, a relatively new, young, but ambitious Romanian startup in the online **movie streaming industry**. WoWCinema’s vision is to make international film content easily accessible to Romanian audiences, with plans to expand across Eastern Europe.

The platform offers a wide range of the latest global releases, flexible subscription plans tailored for different budgets, and AI-driven movie recommendations based on user behavior and preferences. It also provides engagement statistics, personalized dashboards, and a focus on showcasing Romanian cinema alongside international titles.

To succeed in a competitive market, WoWCinema relies on data to guide user engagement, retention, and content acquisition strategies.

As part of the **Data Engineering team**, my role is essential in the development and maintenance of the data infrastructure, which is the backbone of WoWCinema's reporting, analytics, and other internal systems. I work in partnership with data analysts, software engineers, and compliance officers to ensure that data is:

- **Precisely collected** from the right sources (e.g., external databases, internal systems)
- **Securely stored** in a well-structured and scalable data warehouse
- **Efficiently processed** through a robust ETL pipeline
- **Governed and compliant** with applicable data privacy regulations such as GDPR

# Business Context

WoWCinema operates in a dynamic and competitive digital entertainment landscape. The company’s success depends on its ability to:

- Monitor and analyze viewer behavior and engagement in near real-time
- Identify at-risk users and reduce churn through personalized retention strategies
- Generate accurate content performance, licensing and usage reports
- Deliver intelligent movie recommendations powered by AI, tailored to individual user preferences

### ETL pipeline

---

- Extract

  - Scope: This process is performed at the bronze tier level (on raw data), where data is ingested and loaded into raw staging tables without transformations.

- Transform

  - Scope: This process is performed at the silver tier level (on partially cleaned data), where the raw data is cleaned, standardized, and structured into logically related tables.

- Load
  - Scope: This process is performed at the gold tier level, where final views and business-ready tables are created to support the core business goals, reports, dashboards, and KPIs.
