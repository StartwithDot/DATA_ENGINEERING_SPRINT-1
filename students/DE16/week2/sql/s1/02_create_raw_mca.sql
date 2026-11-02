USE DATABASE DE16_WEEK2;
USE SCHEMA DE16_WEEK2.BRONZE;

CREATE TABLE DE16_WEEK2.BRONZE.RAW_MCA_KERALA
(
CIN VARCHAR ,
CompanyName VARCHAR ,
CompanyROCcode VARCHAR ,
CompanyCategory VARCHAR ,
CompanySubCategory VARCHAR ,
CompanyClass VARCHAR ,
AuthorizedCapital VARCHAR ,
PaidupCapital VARCHAR ,
CompanyRegistrationdate_date VARCHAR ,
Registered_Office_Address VARCHAR ,
Listingstatus VARCHAR ,
CompanyStatus VARCHAR ,
CompanyStateCode VARCHAR ,
CompanyIndian_Foreign_Company VARCHAR ,
nic_code VARCHAR ,
CompanyIndustrialClassification VARCHAR
)
;


--why every column is VARCHAR at this stage: we dont have any idea about whats the datatype of each value, so we have to take a look into the datatype of each columns

SELECT * FROM DE16_WEEK2.BRONZE.RAW_MCA_KERALA;