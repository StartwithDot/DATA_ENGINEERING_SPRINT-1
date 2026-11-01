```mermaid
flowchart LR
    A[MCA Company Master Data] --> P[SNOWFLAKE]
    B[IBBI Insolvency Records] --> P
    C[MCA Corporate Data Management Portal] --> P
    E[RBI Policy Rate Data] --> P
    G[AIRFLOW] --> P
    P --> D[DBT]
    G --> D
    D --> U[METABASE]
```