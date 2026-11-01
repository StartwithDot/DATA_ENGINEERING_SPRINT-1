## MCA Company Master Data

MCA stands for ministry of corporate affairs it is the government body that registers every company in india.it assign a 21 character unique number to every company that registers called CIN.For each companyit will provide the CIN, the company name, the registration date, the current status

It answers the question the comapany is really registered and still active

Data are in the form of zip files each zip file contains one Registrar of Companies office, called an RoC

## IBBI Insolvency Records
IBBI stands for Bankruptcy Board of India it look after the bankruptcy proceedings when a company cannot pay their debt they will go through a process called Corporate Insolvency Resolution Process IBBI published the names of companies going through such process

It answers the question that does this company have a record of financial trouble

THE data set is in the form of a pdf need to perfom a python script to change the pdf into proper table structure

## MCA Corporate Data Management Portal
It is a public analylitcs portal in which it has the datas of the active and inactive companies,the details of differents sectors performing, the comparison with public and private sector,also have the state wise performance

It answers the question about how does a company compare to others in its state and industry.

The datas are in the web page so need to run the python script to get in the proper structure

## RBI Policy Rate Data
which decides the repo rate,which is interest rate at which the central bank lends money to the commercial bank

Repo rate is not direct but an indirect tool for calculating how the company has raised so far

The data is in the form of csv some corrections needed

NOTE: the RBI data portal DBIE is now at https://data.rbi.org.in, and the policy rate series only lists the days when the rate changed, so a missing month does not mean missing data. Our downloaded RBI data ends in 2024. That is OK. RBI is background only