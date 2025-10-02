# Script: loan_data_validation.py
# Purpose: Validate and export loan data for audit submission
# Role: Application Support Consultant at Valley Bank
import pandas as pd
import pyodbc

# Connect to SQL Server
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=valley-db;DATABASE=loans;UID=user;PWD=pass")
query = "SELECT loan_id, amount, status, created_date FROM loan_data WHERE status IN ('Approved', 'Pending')"
df = pd.read_sql(query, conn)

# Validate and clean
df["amount"] = df["amount"].apply(lambda x: round(x, 2))
df["created_date"] = pd.to_datetime(df["created_date"])
df.dropna(inplace=True)

# Export for audit
df.to_csv("loan_audit_export.csv", index=False)
print("Export complete.")
