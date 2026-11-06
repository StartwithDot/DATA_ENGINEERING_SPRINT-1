CREATE DATABASE IF NOT EXISTS DE8_WEEK2;
USE DATABASE DE8_WEEK2;

CREATE SCHEMA IF NOT EXISTS DE8_WEEK2.BRONZE;
CREATE SCHEMA IF NOT EXISTS DE8_WEEK2.SILVER;
CREATE SCHEMA IF NOT EXISTS DE8_WEEK2.GOLD;



-- BRONZE: This schema will hold raw, unprocessed data imported from various sources.
-- SILVER: This schema will hold cleaned and transformed data that is ready for further analysis and processing.
-- GOLD: This schema will hold aggregated and curated data for user consumption. It will be used for final reporting and analytics, providing a single source of truth for business insights.
