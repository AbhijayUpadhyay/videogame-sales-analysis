## Optimizing Inventory and Sales Strategies in the Video Game Industry
---
This project analyzes and visualizes data to provide actionable insights for video game developers, publishers, and distributors to optimize sales strategies, enhance customer reach, and boost revenue.

#### Python Libraries:
    `os`, `sqlite3`, ```pandas```, ```numpy```, ```,matplotlib.pyplot```,
#### Custom Modules:
    ```analysis```, ```sql_queries```, ```clean```, ```plots```

### Data Sources
- **vgsales.csv:** Contains historical sales data (e.g., global sales, publisher, platform).
- **games.csv:** Includes metadata about games (e.g., ratings, genre, wishlist count).
- Datasets are joined based on title.

### Usage
1. Ensure required datasets (vgsales.csv and games.csv) are in the root directory.
2. Run the pipeline via ```main.ipynb```

### Components
#### Part One: Setup
- Load Data: Import historical sales (vgsales.csv) and metadata (games.csv) into Pandas DataFrames.
- Clean Data: Use the ```process_dataframe``` function (located in ```clean.py```) to preprocess and clean the datasets.
- Database Setup: Store cleaned data in an SQLite database (videogames.db) with two tables: ```sales``` and ```metadata```.

#### Part Two: SQL Analysis
- Identify trends and patterns in sales data using custom SQL queries.
- All SQL queries can be found in ```sql_queries.py```
- Query results are returned to main.ipynb

#### Part Three: Genre Analysis
- DataFrame manipulation: Combine sales and metadata to identify additional genre-based insights.
- Develop machine learning models to predict sales based on genre, wishlist count, and other features.

### Contributors
Abhijay Upadhyay - au143

Luke Fernandez - lmf232
