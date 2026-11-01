MCA Company Master Data
What it is : Its usually a government under control site. MCA stands for  Ministry Of Corporate Affairs. in this site each company holds a CIN number just like an id  so this MCA publishes all the list of all registered company all over india (datagov.in )-its a government  portal

Why it matters to the client :totally it hold 31 lakh companies data out of 31 only 20lakh companies are registered so this platform help to know whether the company is registered or genuine.

How it arrives:  it contains 20 to 25 zip files.Each ZIP covers one Register of Companies office, called an RoC. Inside each ZIP is one CSV file. CSV means comma separated values, a plain text table format.The data will be messy.


2.IBBI Insolvency Records
What it is:  its also a government controlled body which help to the overseas bankruptcy. when a company fails to pay its debts it takes action and files cases againist the company called as CIRP process.

Why it matters to the client:To know about the company financial issues and debt cases  a company which have insolvency records is highly risk to lending money.

How It Arrives: as a PDF file on the IBBI website.looks like a printed page. no csv download or APIs so needed python program to extract.

3.MCA Corporate Data Management Portal

What is it: it runs a  public analytics portal at mcacdm.nic.in. It shows summary statistics about companies in India . it also shows number of company registered in each state.

Why it matters to the client: it helps to compare to its surroundings. Knowing that a company is registered in TamilNadu is more useful when you also know how many active companies the state has and which industries dominate there.

How it arrives. simple HTML tables on web pages. HTML is the language web pages are created no downloading options available.

4.RBI Policy Rate Data
What it is : it gives the interest rate at which it lends to banks. This rate shapes borrowing costs across the whole economy.  data.rbi.org.in it is the data portal to see the details.

Why it matters to the client:  it gives answer like "what was the repo rate when this company was incorporated". It is not company level data, so we use it as supporting context, not as a core part of the risk model.

How it arrives: As downloadable Excel or CSV files git. The files need light cleaning: merged cells in Excel, percentage symbols attached to numbers, and dates in Indian formats.