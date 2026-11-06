```mermaid
flowchart LR
    A[ MCA Company Master Data] --> P[SNOWFLAKE]
    B[ IBBI Insolvency Records] --> P
    C[MCA Corporate Data Management Portal] --> P
    D[RBI Policy Rate Data] --> P
    P --> E[DBT]
    G[AIRFLOW] --> P
    G[AIRFLOW] --> E
    E[DBT] --> F[METABASE]
    F -->X[USER]
```
