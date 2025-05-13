# World-GDP-ETL-Pipeline
This project automates the process of scraping GDP data from a Wikipedia archive, filters countries with a GDP over $100 billion, stores the cleaned data in a local SQLite database, and visualizes the top 10 economies. A cron job is also set up to run the ETL pipeline on a scheduled basis.

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

### Visualization Top 10 Countries by GDP
The bar chart below shows the top 10 economies based on GDP (in USD billions).
This was generated as part of the transformation and analysis step.

![Image](https://github.com/user-attachments/assets/a27020fe-8351-4907-9655-d9f8902411f5)
