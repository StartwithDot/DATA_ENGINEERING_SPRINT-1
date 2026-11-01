    use database DE14_WEEK2;
use schema DE14_WEEK2.BRONZE;

 create table DE14_WEEK2.BRONZE. RAW_MCA_KERALA
 (
CIN varchar,
CompanyName varchar,
CompanyROCcode varchar,
CompanyCategory varchar,
CompanySubCategory varchar,
CompanyClass varchar,
AuthorizedCapital varchar,
PaidupCapital varchar,
CompanyRegistrationdate_date varchar,
Registered_Office_Address varchar,
Listingstatus varchar,
CompanyStatus varchar,
CompanyStateCode varchar,
CompanyIndian_Foreign_Company varchar,
nic_code varchar,
CompanyIndustrialClassification  varchar 

 );
 --why every column is VARCHAR at this stage.. we dont know about what kind of datatype of each values so we use varchar
 
 select * from DE14_WEEK2.BRONZE. RAW_MCA_KERALA;
 