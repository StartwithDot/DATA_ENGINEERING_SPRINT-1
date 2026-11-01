USE DATABASE DE4_WEEK2;
USE SCHEMA BRONZE;

CREATE TABLE DE4_WEEK2.BRONZE.RAW_MCA_KERALA
(
    CIN VARCHAR,
    CompanyName VARCHAR,
    CompanyRegistrationdate_date VARCHAR,
    CompanyROCcode VARCHAR,
    CompanyCategory VARCHAR,
    CompanySubCategory VARCHAR,
    CompanyClass VARCHAR,
    AuthorizedCapital VARCHAR,
    PaidCapital VARCHAR,
    Registered_office_Address VARCHAR,
    Listingstatus VARCHAR,
    CompanyStatus VARCHAR,
    CompanyStatusCode VARCHAR,
    CompanyIndianForeign_Company VARCHAR,
    nic_code VARCHAR,
    CompanyIndustrialClassification VARCHAR
    
);

-- Why every column is VARCHAR at this stage: we o't know which datatype is used, So we take datatyp varchar

SELECT * from DE4_WEEK2.BRONZE.RAW_MCA_KERALA;