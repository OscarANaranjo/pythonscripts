# Script: crm_mailchimp_integration.py
# Role: Salesforce Business Analyst at Kallman Worldwide
# Purpose: Extract campaign KPIs (open rate, click rate) from Mailchimp and prepare for integration with Momentus CRM
# Technologies: Python, REST API, JSON, requests
# Business Impact: Enabled marketing teams to visualize campaign performance and reduce manual reporting overhead
import requests
import json

# Mailchimp API setup
api_key = "your_mailchimp_api_key"
server_prefix = "usX"  # e.g., us19
list_id = "abc123"

# Fetch campaign reports
url = f"https://{server_prefix}.api.mailchimp.com/3.0/reports"
headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(url, headers=headers)

# Parse and push to CRM
for campaign in response.json().get("reports", []):
    kpi_data = {
        "campaign_id": campaign["id"],
        "open_rate": campaign["opens"]["open_rate"],
        "click_rate": campaign["clicks"]["click_rate"]
    }
    # Simulated CRM push
    print(f"Pushing to CRM: {kpi_data}")
