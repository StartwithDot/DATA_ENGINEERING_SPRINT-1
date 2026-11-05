## OBJECTIVE

As our client is a fintech due diligence , means checking a business before trusting it. Their customers are lenders, banks, and procurement teams. For that Client we are building a reliable due diligence platform to simply monitor different companies current status,history and finacial risks incorprated by collecting and transforming different real data sources which helps to decide on lending ,buying and signing contracts.

### 4 MAJOR DATA SOURCES FOR PLATFORM

##### MCA Company Master Data :
- Data of every registered company in India and each company have a 21 character primary id as a unique identifier called CIN number (Corporate Identity Number)- https://data.gov.in
- Data arrives as 20 to 25 separate `ZIP files` published roughly monthly

##### IBBI Insolvency Records :
- Data of every company that goes through the Corporate Insolvency Resolution Process, called CIRP;When a company cannot pay its depts - https://ibbi.gov.in
- Data arrives as `PDF files` every quarter.

##### MCA Corporate Data Management Portal:
- Data of economic backdrop of a company like how many active companies each state has, how company counts are split across industries, how capital is distributed, and filing trends over the years- https://mcacdm.nic.in
- Data as in `HTML tables` , we needed to webscrape using Python.

##### RBI Policy Rate Data :
- Data about company (repurchase rate)Repo Rates (The interest rate at which the RBI lends short-term funds) ,this rate shapes borrowing costs across the whole economy. -https://data.rbi.org.in
- Data arrives as downloadable Excel or `CSV files`.

## CLIENT DELIVERY AGENDA

- They want the history kept, so they can answer not just "what is this company's status today" but "what was this company's status three months ago". 
- They want the whole thing to refresh on a regular schedule. 
- They want a dashboard at the end that a non technical person can use.

## SIMPLIFIED PIPELINE
Data collection -->ELT--->Snowflake-->DBT layers-->Metabase-->User

## FINAL OUTPUT

An automated single dashboard that refreshes daily that also shows history data for daily analysts , lenders, banks, and procurement teams for do finacial due diligence on companies through a user-friendly dashboard that a non technical person can use.