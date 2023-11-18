import pandas as pd
import json

# Read Excel file
excel_file = 'demo.xlsx'
df = pd.read_excel(excel_file)

# Convert DataFrame to JSON
json_data = df.to_json(orient='records', indent=4)

# Save JSON data to a file
json_file = 'output.json'
with open(json_file, 'w') as f:
    f.write(json_data)

print("JSON data saved to", json_file)
