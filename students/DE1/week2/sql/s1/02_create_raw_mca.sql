use database DE1_WEEK2;
use schema DE1_WEEK2.BRONZE;

create table DE1_WEEK2.BRONZE.raw_mca_kerala
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
CompanyIndustrialClassification varchar
) 
;

 -- Why every column is VARCHAR at this stage: sice we dont know about the datatype of each colums we used varchar for now
select*from DE1_WEEK2.BRONZE.RAW_MCA_KERALA;


