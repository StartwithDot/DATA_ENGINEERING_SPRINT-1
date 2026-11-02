1. MCA Company Master Data

What it is: The Ministry of Corporate Affairs (MCA) is the official government registry that records every legal company in India.

Which client question it answers: It answers if a company is real, legally registered, and currently active or closed.

How it arrives: It arrives roughly once a month as 20 to 25 ZIP files containing CSV tables.


2. IBBI Insolvency Records

What it is: The Insolvency and Bankruptcy Board of India (IBBI) tracks businesses that cannot pay their debts and go through bankruptcy court.

Which client question it answers: It answers if a company has ever faced serious financial trouble or insolvency proceedings.

How it arrives: It arrives roughly every three months as PDF documents that require Python to extract the tables.


3. MCA Corporate Data Management Portal

What it is: The MCA CDM portal is a government website that shows company counts and business statistics across Indian states and sectors.

Which client question it answers: It answers how a company compares to its competitors and surroundings in its home state.

How it arrives: It arrives as HTML tables on web pages with no download button, so we extract the numbers using Python.


4. RBI Policy Rate Data

What it is: The Reserve Bank of India (RBI) is the central bank that sets the benchmark interest rate for borrowing money.

Which client question it answers: It answers what the economic borrowing conditions were like when a company was first started.

How it arrives: It arrives as downloadable CSV or Excel files from the RBI data portal whenever policy interest rates change.