```mermaid
flowchart LR
    A[MCA Company Master Data] --> P[SNOWFLAKE]
    B[IBBI Insolvency Records] --> P
    C[MCA Corporate Data Management Portal] --> P
    D[RBI Policy Rate Data] --> P
    P --> E[DBT]
    Z[AIRFLOW] --> E
    Z[AIRFLOW] --> P
    E --> F[METABASE]
```