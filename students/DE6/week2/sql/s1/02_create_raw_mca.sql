use database de6_week2;
use warehouse DD_WH_DE6;
USE SCHEMA DE6_WEEK2.BRONZE;



create table if not exists de6_week2.bronze.RAW_MCA_kerala(
    
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
    
    );

    select * from de6_week2.bronze.raw_mca_kerala limit 5;

    
    -- Table: BRONZE.RAW_MCA_KERALA
    -- Why every column is VARCHAR at this stage:beacuse we dont know about which datatype this source carrying