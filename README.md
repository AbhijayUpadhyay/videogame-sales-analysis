## Optimizing Inventory and Sales Strategies in the Video Game Industry
---
This project analyzes and visualizes data to provide actionable insights for video game developers, publishers, and distributors to optimize sales strategies, enhance customer reach, and boost revenue.

### Libraries
- ```os```, ```sqlite3```, ```pandas```, ```numpy```, ```matplotlib.pyplot```
- Custom modules: ```analysis```, ```sql_queries```, ```clean```

### Usage
- Run ```main.ipynb``` as normal.

### Components
##### Part One: Setup
- Load historical sales (vgsales.csv) and metadata (games.csv) datasets into Pandas DataFrames.
- ```process_dataframe```: Cleans the data. Located in clean.py.
- Store cleaned data in an SQLite database (videogames.db) for analysis.
- Tables: ```sales``` and ```metadata```

##### Part Two: SQL Analysis
- All SQL queries can be found in ```sql_queries.py```
- Query results are returned to main.ipynb

##### Part Three: Genre Analysis

