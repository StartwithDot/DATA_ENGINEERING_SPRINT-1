```mermaid
flowchart LR
    A[MCA] --> P[Snowflake]
    B[IBBI] --> P
    C[MCA COMPANY DATA MANAGMENT] --> P
    E[RBI Policy rate Data] --> P
    P --> D[Dbt]
    D --> U[MetaBase]
    Z[AirFlow] --> D
    Z --> P
```