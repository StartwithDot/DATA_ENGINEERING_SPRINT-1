## MCA Company Master Data

MCA stands for ministry of corporate affairs it is the government body that registers every company in india.it assign a 21 character unique number to every company that registers called CIN.For each companyit will provide the CIN, the company name, the registration date, the current status

It answers the question the comapany is really registered and still active

Data are in the form of zip files each zip file contains one Registrar of Companies office, called an RoC

## IBBI Insolvency Records

The Insolvency and Bankruptcy Board of India (IBBI) tracks businesses that cannot pay their debts and go through bankruptcy court.

It answers if a company has ever faced serious financial trouble or insolvency proceedings.

It arrives roughly every three months as PDF documents that require Python to extract the tables.

## MCA Corporate Data Management Portal

It is a public analylitcs portal in which it has the datas of the active and inactive companies, the details of differents sectors performing, the comparison with public and private sector, also have the state wise performance

It answers the question about how does a company compare to others in its state and industry.

The datas are in the web page so need to run the python script to get in the proper structure

## RBI Policy Rate Data

 It sets the repo rates to the banks, suppose if the economy is going through a inflation the RBI will set the repo rates high which will forces the banks to lend monwy with high interest also if the economy is going to crisis the RBI will reduce the rates so that banks can reduce the interest rate. Knowing the repo rate at the exact time a company was registered gives lenders a quick snapshot of the economic condition — whether money was expensive or cheap when that business first opened its doors. It comes as a CSV file but it needs some 

 NOTE : The RBI data portal DBIE is now at https://data.rbi.org.in, and the policy rate series only lists the days when the rate changed, so a missing month does not mean missing data. Our downloaded RBI data ends in 2024. That is OK. RBI is background only.