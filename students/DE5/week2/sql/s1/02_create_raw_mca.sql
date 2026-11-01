USE DATABASE DE05_WEEK2;
USE SCHEMA DE05_WEEK2.BRONZE;

CREATE TABLE DE05_WEEK2.BRONZE.RAW_MCA_KERALA
(
    CIN VARCHAR,
    CompanyName VARCHAR,
    CompanyRegistrationdate_date VARCHAR,
    CompanyROCcode VARCHAR,
    CompanyCategory VARCHAR,
    CompanySubCategory VARCHAR,
    CompanyClass VARCHAR,
    AuthorizedCapital VARCHAR,
    PaidupCapital VARCHAR,
    Registered_Office_Address VARCHAR,
    Listingstatus VARCHAR,
    CompanyStatus VARCHAR,
    CompanyStateCode VARCHAR,
    CompanyIndian_Foreign_Company VARCHAR,
    nic_code VARCHAR,
    CompanyIndustrialClassification VARCHAR
);

-- Why every column is VARCHAR at this stage: we don't have any idea about datatype of each values so we have to take a look into the datatype of each coloumns.

SELECT * FROM DE5_WEEK2.BRONZE.RAW_MCA_MCA_KERALA;