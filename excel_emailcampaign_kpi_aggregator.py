# Script: excel_emailcampaign_kpi_aggregator.py
# Purpose: Aggregate email campaign KPIs (opens, clicks) by contact and export to Excel for CRM ingestion
# Technologies: Python, pandas, openpyxl
# Business Impact: Simplifies data prep for Momentus CRM and Salesforce by consolidating engagement metrics into a clean Excel format

import pandas as pd

# Load raw CSV file with email campaign metrics
input_file = "raw_campaign_data.csv"
df = pd.read_csv(input_file)

# Optional: clean column names for consistency
df.columns = [col.strip().title() for col in df.columns]

# Deduplicate by Email and aggregate Opens and Clicks
aggregated = (
    df.groupby("Email", as_index=False)
    .agg({
        "Account": "first",     # Preserve first account code per email
        "Name": "first",        # Preserve first name
        "Company": "first",     # Preserve first company
        "Title": "first",       # Preserve first title
        "Opens": "sum",         # Sum total opens
        "Clicks": "sum"         # Sum total clicks
    })
)

# Export to Excel for CRM ingestion
output_file = "ExcelKPILoad.xlsx"
aggregated.to_excel(output_file, index=False)

print(f"Aggregated KPI file saved to {output_file}")
