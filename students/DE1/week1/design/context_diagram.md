```mermaid
flowchart LR
    A[MCA Company Master Data] --> P[SNOWFLAKE]
    B[IBBI Insolvency Records] --> P
    C[MCA Corporate Data Management Portal] --> P
    F[RBI Policy Rate Data]-->P
    G[AIRFLOW]-->P
    %% Add the fourth source yourself.
    P --> D[DBT]
    D --> U[METABASE]
    G-->D
```