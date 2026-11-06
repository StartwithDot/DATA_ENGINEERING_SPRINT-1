## DATA SOURCES AND SUMMARY 

#### MCA Company Master Data :

*  Data of every registered company in India and each company have a 21 character primary id as a unique identifier called CIN number (Corporate Identity Number)-  https://data.gov.in

- Data answers about the company is real and what is its current status 

- Data arrives as 20 to 25 separate ZIP files published roughly `monthly`. Each ZIP covers one Registrar of Companies office, called an RoC. Inside each ZIP is one CSV file.


####  IBBI Insolvency Records :
- Data of every company that goes through the Corporate Insolvency Resolution Process, called CIRP;When a company cannot pay its depts - https://ibbi.gov.in
- Data answers about whether the company is in any critical finacial trouble
- Data arrives as PDF files on roughly `every quarter`.


####  MCA Corporate Data Management Portal:
- Data of economic backdrop of a company like how many active companies each state has, how company counts are split across industries, how capital is distributed, and filing trends over the years- https://mcacdm.nic.in
- Data answers about how does a company to its surroundings 
- Data as in HTML tables in website we needed to webscrape for collecting data

####  RBI Policy Rate Data :

- Data about comapany (repurchase rate)Repo Rates (The interest rate at which the RBI lends short-term funds) ,this rate shapes borrowing costs across the whole economy.

Note: the RBI data portal DBIE is now at https://data.rbi.org.in, and the policy rate series only lists the days when the rate changed, so a missing month does not mean missing data. Our downloaded RBI data ends in 2024. That is OK. RBI is background only

- Data is just light background context about which was the repo rate when a particular company was incorporated.
- Data arrives as downloadable Excel or CSV files.