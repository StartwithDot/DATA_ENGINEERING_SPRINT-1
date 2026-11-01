1----
Our client is a fintech due diligence company. Due diligence means checking a business before trusting it. Their customers are lenders, banks, and procurement teams. Before a customer lends money to a company, or buys from a company, or signs a contract with a company, they want to know three things.

2----
First, a working data pipeline. It refreshes the registry monthly, the insolvency data quarterly, and the context sources on their own schedules. Every run is logged, checked, and reproducible. If a source publishes a bad file, the pipeline stops and says so, instead of quietly loading wrong data.

Second, a set of gold layer tables the client can query directly: the company dimension with full status history, the insolvency event facts, the state level context. These tables are documented, tested, and stable.

Third, a Metabase dashboard for everyday use. A due diligence analyst can search a company, see its current status, see its status history, see any insolvency events, and see how it compares to its state and industry. That is the product the client asked for on the start, and every task group on the roadmap exists to make it trustworthy.


3---
we use 4 sources of data
MCA Company Master Data
IBBI Insolvency Records
MCA Corporate Data Management Portal
RBI Policy Rate Data

4---
a finsihed product will look like:
Metabase dashboard for everyday use. A due diligence analyst can search a company, see its current status, see its status history, see any insolvency events, and see how it compares to its state and industry