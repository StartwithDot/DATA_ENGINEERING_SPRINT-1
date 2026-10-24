MCA Company Master Data
What it is. The Ministry of Corporate Affairs, called MCA, is the government body that registers every company in India. Every company gets a 21 character identification number called a CIN, which stands for Corporate Identity Number. The MCA publishes a master list of all registered companies on data.gov.in, India's open government data platform.

Why it matters to the client. This is the core of the platform. It answers the first question: is this company real and what is its status. The registry holds roughly 31 lakh companies in total, of which roughly 20 lakh are active.

How it arrives. As roughly 20 to 25 separate ZIP files. Each ZIP covers one Registrar of Companies office, called an RoC. Inside each ZIP is one CSV file. CSV means comma separated values, a plain text table format. The files arrive with messy details: state names written differently across files, dates in different formats, capital amounts with commas and currency symbols mixed in. Each update is a full fresh snapshot of the whole registry, published roughly monthly.


IBBI Insolvency Records
What it is. The Insolvency and Bankruptcy Board of India, called IBBI, is the government body that oversees bankruptcy proceedings. When a company cannot pay its debts, it can enter a legal process called the Corporate Insolvency Resolution Process, called CIRP. The IBBI publishes lists of companies going through this process.

Why it matters to the client. This answers the second question: has this company been in serious financial trouble. A company in insolvency proceedings is a high risk company to lend to. This is the most important risk signal in the whole platform. Because each row carries a CIN, we can attach each insolvency event to the right company in the MCA registry.

How it arrives. As PDF files on the IBBI website, published roughly every quarter. A PDF is a document format made for reading, not for data work. The table of companies is inside the PDF as text laid out like a printed page. There is no CSV download and no download API. We must write a small Python program to read the PDF and pull the table out into a CSV file.




MCA Corporate Data Management Portal
What it is. The MCA runs a public analytics portal at mcacdm.nic.in. It shows summary statistics about companies in India: how many active companies each state has, how company counts are split across industries, how capital is distributed, and filing trends over the years.

Why it matters to the client. This answers the third question: how does this company compare to its surroundings. Knowing that a company is registered in Kerala is more useful when you also know how many active companies Kerala has and which industries dominate there. It gives every company record an economic backdrop.

How it arrives. As HTML tables on web pages. HTML is the language web pages are written in. There is no download button and no data file. We must write a small Python program that reads the web page and pulls the numbers out of the tables.


RBI Policy Rate Data
What it is. The Reserve Bank of India, called RBI, is India's central bank. It sets the repo rate, which is the interest rate at which it lends to banks. This rate shapes borrowing costs across the whole economy. The RBI publishes its data through a portal called the Database on the Indian Economy, called DBIE, at data.rbi.org.in (older pages call it dbie.rbi.org.in).

Why it matters to the client. This is light background context only. It lets the platform answer questions like "what was the repo rate when this company was incorporated". It is not company level data, so we use it as supporting context, not as a core part of the risk model.

How it arrives. As downloadable Excel or CSV files from the DBIE portal. The files need light cleaning: merged cells in Excel, percentage symbols attached to numbers, and dates in Indian formats.