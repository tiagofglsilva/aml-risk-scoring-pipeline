import os
import sqlite3
import pandas as pd
import kagglehub

# Path Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)
db_path = os.path.join(DATA_DIR, "aml.db")

print(f"--> Saving database to: {db_path}")

# 2. Download and reading the dataset from Kaggle
print("--> Downloading/loading dataset from Kaggle...")
path = kagglehub.dataset_download("shrutimechlearn/churn-modelling")
csv_path = os.path.join(path, "Churn_Modelling.csv")

df = pd.read_csv(csv_path)
print(f"--> CSV file read successfully ({len(df)} rows).")

# 3. Saving the DataFrame to SQLite database
conn = sqlite3.connect(db_path)
df.to_sql("customers", conn, if_exists="replace", index=False)

# Storing
conn.commit()
conn.close()

# Confirmation message
if os.path.exists(db_path):
    size_bytes = os.path.getsize(db_path)
    print(f"--> Completed! The file aml.db exists and has a size of: {size_bytes / 1024:.2f} KB")