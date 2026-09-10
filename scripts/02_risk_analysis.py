import os
import sqlite3
import pandas as pd
from tabulate import tabulate

#Dataset connection
SCRIPT_DIR=os.path.dirname(os.path.abspath(__file__))
BASE_DIR=os.path.dirname(SCRIPT_DIR)
db_path=os.path.join(BASE_DIR, "data", "aml.db")
reports_dir=os.path.join(BASE_DIR, "reports")
conn=sqlite3.connect(db_path)

risk_score_query="""
    SELECT
        CustomerId,
        Surname,
        Geography,
        Age,
        Balance,
        EstimatedSalary,
        ROUND(Balance/EstimatedSalary, 2) AS BalanceToSalaryRatio
    FROM customers
    WHERE
        -- Filter 1: Balance above five years of salary
        Balance > 5 * EstimatedSalary

        -- Filter 2: Exclude salary below 500
        AND EstimatedSalary > 500
        
        -- Filter 3: Age above or equal to 18
        AND Age >= 18

        -- Filter 4: Minimum balance threshold
        AND Balance > 50000
        
        -- Filter 5: Balance greater than could have accumulated based on age and salary
        AND Balance > (Age - 18) * EstimatedSalary
        
    ORDER BY 
        BalanceToSalaryRatio DESC
"""
#Results
df_escalations=pd.read_sql_query(risk_score_query, conn)

conn.close()

print("===Clients with high risk score based on balance to salary ratio===")
print(tabulate(df_escalations, headers='keys', tablefmt='psql', showindex=False))

#Aditional analysis: Count of high risk clients by geography
print("===Summary of high risk clients by geography===")
summary_by_geography=df_escalations.groupby("Geography")[["Balance","EstimatedSalary","BalanceToSalaryRatio"]].mean().round(2)
print(tabulate(summary_by_geography, headers='keys', tablefmt='psql'))

print("===Top 5 Clients with highest balance to salary ratio===")
top_ratio=df_escalations.nlargest(5, "BalanceToSalaryRatio")[["CustomerId","Surname","Geography","Age","BalanceToSalaryRatio"]]
print(tabulate(top_ratio, headers='keys', tablefmt='psql', showindex=False))

corr=df_escalations["Age"].corr(df_escalations["BalanceToSalaryRatio"])
print(f"===Correlation between Age and Balance to Salary Ratio: {corr:.2f}===")

#Export
os.makedirs(reports_dir, exist_ok=True)
report_path=os.path.join(reports_dir, "high_risk_clients.csv")
df_escalations.to_csv(report_path, index=False)

print(f"Report exported to: {report_path}")


