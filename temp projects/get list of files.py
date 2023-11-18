import boto3
from urllib.parse import urlparse


# Parse the S3 URL to extract the bucket name and prefix (folder)
s3_url = "s3://uniqusai-gpt-prod/big4/deloitte/deloitte3"
parsed_url = urlparse(s3_url)
bucket_name = parsed_url.netloc
prefix = parsed_url.path.lstrip('/')
arr=[]
temp_arr=[]
# Initialize the S3 client
s3_client = boto3.client('s3')

# Use the list_objects_v2 function to list objects in the bucket
response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

# Extract and print the list of object keys (file paths)
if 'Contents' in response:
    file_paths = [obj['Key'] for obj in response['Contents']]
    for f,file_path in enumerate(file_paths):
        print(file_path)
        if f==0:
            continue
        temp_arr.append(str(file_path).replace('big4/deloitte/deloitte3/',''))
        arr.append(temp_arr)
        temp_arr=[]
        
else:
    print("No files found in the specified S3 bucket.")
# print(arr)
# w_excel([arr])



import pandas as pd

# Your list of data
data = ['0390226c-770a-4eec-890c-208fc8f7f592']

# Create a DataFrame from the data
df = pd.DataFrame(arr, columns=["Column Name"])

# Specify the Excel file path
excel_file_path = "data.xlsx"  # Change this to the desired file path

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False, engine="openpyxl")

print("Data written to the Excel file successfully.")

