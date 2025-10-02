# Script: epm_metadata_checker.py
# Role: Oracle EPM Support Analyst at Xylem Inc.
# Purpose: Parse Hyperion metadata files to identify missing account mappings for financial reporting
# Technologies: Python, file I/O, regex, logging
# Business Impact: Improved metadata integrity and reduced manual validation effort across EPM infrastructure
import os
import re

# Read metadata file
with open("/opt/hyperion/metadata/account_mappings.txt", "r") as file:
    lines = file.readlines()

# Parse and validate
missing = []
for line in lines:
    if not re.search(r"Account:\s+\w+\s+->\s+\w+", line):
        missing.append(line.strip())

# Log results
if missing:
    with open("missing_mappings.log", "w") as log:
        for item in missing:
            log.write(f"Incomplete mapping: {item}\n")
    print(f"{len(missing)} mappings missing. Logged.")
else:
    print("All mappings valid.")
