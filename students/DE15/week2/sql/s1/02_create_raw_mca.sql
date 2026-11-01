use database DE15_WEEEK2;
use schema DE15_WEEEK2.BRONZE;

CREATE TABLE DE15_WEEEK2.BRONZE.RAW_MCA_KERALA
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

-- Why every column is VARCHAR at this stage: We dont have any idea bout whats the datatype of each values , so we have to take a look into the datatype of each columns

SELECT * FROM DE15_WEEEK2.BRONZE.RAW_MCA_KERALA;