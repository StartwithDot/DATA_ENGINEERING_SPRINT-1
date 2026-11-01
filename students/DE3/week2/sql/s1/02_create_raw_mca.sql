CREATE TABLE DE03_WEEK2.BRONZE.RAW_MCA_KERALA (
    CIN VARCHAR,
    CompanyName VARCHAR,
    CompanyROCcode VARCHAR,
    CompanyCategory VARCHAR,
    CompanySubCategory VARCHAR,
    CompanyClass VARCHAR,
    AuthorizedCapital VARCHAR,
    PaidupCapital VARCHAR,
    CompanyRegistrationdate_date DATE,
    Registered_Office_Address VARCHAR,
    Listingstatus VARCHAR,
    CompanyStatus VARCHAR,
    CompanyStateCode VARCHAR,
    CompanyIndian_Foreign_Company VARCHAR,
    nic_code VARCHAR,
    CompanyIndustrialClassification VARCHAR
);
select * from DE03_WEEK2.BRONZE.RAW_MCA_KERALA;
 -- TODO: one VARCHAR column per field in your CSV header
 -- Why every column is VARCHAR at this stage: because we dont know whether the data is in number or text format.