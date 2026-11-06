-- Table: BRONZE.RAW_MCA_KERALA

USE DATABASE DE8_WEEK2;
USE SCHEMA DE8_WEEK2.BRONZE;

CREATE TABLE DE8_WEEK2.BRONZE.RAW_MCA_KERALA
(
CIN VARCHAR ,
CompanyName VARCHAR,
CompanyROCcode VARCHAR ,
CompanyCategory VARCHAR,
CompanySubCategory VARCHAR ,
CompanyClass VARCHAR,
AuthorizedCapital VARCHAR ,
PaidupCapital VARCHAR,
CompanyRegistrationdate_date VARCHAR ,
Registered_Office_Address VARCHAR,
Listingstatus VARCHAR ,
CompanyStatus VARCHAR,
CompanyStateCode VARCHAR ,
CompanyIndian_Foreign_Company VARCHAR,
nic_code VARCHAR ,
CompanyIndustrialClassification VARCHAR
)
;
    
 -- Why every column is VARCHAR at this stage: VARCHAR MEANS VARIABLE CHARACTER, which means that the column can hold any type of data, including text, numbers, and special characters. Since we don't know the data types of each column in the CSV file, we use VARCHAR to ensure that we can store all types of data without any issues.

SELECT * FROM BRONZE.RAW_MCA_KERALA LIMIT 5;