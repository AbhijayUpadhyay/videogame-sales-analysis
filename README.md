# Optimizing Inventory and Sales Strategies in the Video Game Industry
---
This project analyzes and visualizes data to provide actionable insights for video game developers, publishers, and distributors to optimize sales strategies, enhance customer reach, and boost revenue.

### Contributors:
- Abhijay Upadhyay - au143
- Luke Fernandez - lmf232

### Python Libraries:
```os```, ```sqlite3```, ```pandas```, ```numpy```, ```matplotlib.pyplot```, ```sklearn.linear_model```, ```sklearn.metrics```
### Custom Modules:
```analysis```, ```sql_queries```, ```clean```, ```plots```

### Data Sources
- **vgsales.csv:** Contains historical sales data (e.g., global sales, publisher, platform).
- **games.csv:** Includes metadata about games (e.g., ratings, genre, wishlist count).

### Folder Structure
```
.
├── main.ipynb               # Jupyter Notebook pipeline to run the analysis
├── analysis.py              # Custom module for analysis functions
├── clean.py                 # Custom module for data processing functions
├── sql_queries.py           # Custom module for SQL queries
├── games.csv                # Dataset containing game metadata (ratings, genre, etc.)
├── vgsales.csv              # Dataset containing historical sales data (global sales, publisher, platform, etc.)
├── images/                  # Folder to store plot images (e.g., figures generated by matplotlib)
└── requirements.txt         # List of all required Python packages
└── README.md                # Project documentation (this file)

```

---

## Getting Started
### Option 1 (Recommended): Running on Rutgers JupyterLab
#### Step 1: Access the Rutgers JupyterLab Environment
- Visit the Codebench JupyterLab portal.
- Log in with your Rutgers credentials.

#### Step 2: Upload the Project Files 
- Upload the project files (e.g., main.ipynb, analysis.py, sql_queries.py, clean.py, etc.) to your JupyterLab workspace.
  - This can be done  by dragging and dropping the files into the file explorer in JupyterLab.

#### Step 3: Run the Notebook
- Execute main.ipynb Jupyter Notebook cell by cell and observe the results.

### Option 2: Set Up a Virtual Environment
#### Step 1: Clone the repository
Start by cloning the repository to your local machine.
```
git clone https://github.com/lukerepublic/videogame-sales-analysis.git
cd videogame-sales-analysis
```

#### Step 2: Set up a Python Virtual Environment
If you don't have ```virtualenv``` installed, you can install it via ```pip```
```
pip install virtualenv
```
Create the virtual environment:
```
python3 -m venv venv
```
Activate the environement:
```
# On macOS/Linux
source venv/bin/activate

# On Windows
.\venv\Scripts\activate
```

#### Step 3: Install Dependencies
Once the virtual environment is activated, install the required packages from ```requirements.txt```.
```
pip install -r requirements.txt
```

#### Step 4: Setting up the Notebook
Ensure that you have Jupyter Notebook installed in your virtual environment. If it's not installed, you can install it using:
```
pip install notebook
```

Now, start Jupyter Notebook:
```
jupyter notebook
```
This will open Jupyter in your web browser. Open the main.ipynb file, and you can start running the notebook.


#### Step 5: Run the Notebook
Open and execute main.ipynb Jupyter Notebook cell by cell and observe the results.

---

## Example Workflow in ```main.ipynb```
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

#### Part Four: Predictive Modeling
- Predict the outcome of games released in a given year and average plays by month and a publisher's sales given the number of games they've released and draw conclusions.

#### Part Five: Our suggestions based on our analysis
- Give suggestions and insights to both physical retailers and game developers, distributors, and publishers on how to maximize sales
- based off what factors correlate positively and heavily with number of sales and plays

---

### Demo
- Here's the link to our video for the project: https://youtu.be/skJIfz-B4ZI


  
