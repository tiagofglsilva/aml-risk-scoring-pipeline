import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

conn=sqlite3.connect(os.path.join(DATA_DIR, "aml.db"))

#Only High Risk Clients
risk_query = """
    SELECT
        CustomerId, Surname, Geography, Age, Balance, EstimatedSalary,
        ROUND(Balance/EstimatedSalary, 2) AS BalanceToSalaryRatio
    FROM customers
    WHERE
        Balance > 5 * EstimatedSalary
        AND EstimatedSalary > 500
        AND Age >= 18
        AND Balance > 50000
        AND Balance > (Age - 18) * EstimatedSalary
"""

df_risk = pd.read_sql_query(risk_query, conn)
conn.close()

sns.set_theme(style="whitegrid")

#Graph 1: Age & Geography
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df_risk,
    x="Age",
    y="BalanceToSalaryRatio",
    hue="Geography",
    size="Balance",
    sizes=(40,200),
    palette="Set2",
)
plt.title("High Risk Clients: Age vs Balance to Salary Ratio by Geography")
plt.xlabel("Age")
plt.ylabel("Balance to Salary Ratio")
plt.tight_layout()
plt.savefig(os.path.join(REPORTS_DIR, "age_geography_risk.png"), dpi=300)
plt.close()

#Graph 2: Mean ratio by Geography
plt.figure(figsize=(6, 4))
sns.barplot(
    data=df_risk,
    x="Geography",
    y="BalanceToSalaryRatio",
    hue="Geography",
    estimator="mean",
    errorbar=None,
    palette="viridis",
    legend=False
)
plt.title("Mean Balance to Salary Ratio by Geography")
plt.ylabel("Mean Ratio")
plt.tight_layout()
plt.savefig(os.path.join(REPORTS_DIR,"geo_risk_summary.png"),dpi=300)
plt.close()

print("Graphs succesfully created")
