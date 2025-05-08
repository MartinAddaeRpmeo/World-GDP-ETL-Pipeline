# World-GDP-ETL-Pipeline
This project automates the process of scraping GDP data from a Wikipedia archive, filters countries with a GDP over $100 billion, stores the data in a local database, and visualizes the top 10 economies.
It includes a cron job setup to schedule the ETL pipeline automatically.

### Project Features
scrape GDP data from Wikipedia

Clean and transform data

Save raw data as CSV

Load cleaned data into SQLite

Visualize the top 10 countries by GDP

Schedule the ETL with cron

### Technologies Used
Python
BeautifulSoup & Requests – scraping
Pandas – data manipulation
SQLite & SQLAlchemy – database storage
Matplotlib / Seaborn – visualization
cron – scheduling automation
Logging – process monitoring
