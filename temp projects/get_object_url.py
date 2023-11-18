import boto3
import openpyxl
from datetime import datetime, timedelta
import urllib.parse

from write import write_to_excel


# Specify the file path of your Excel file
file_path = '../Big 4.xlsx'

# Load the Excel workbook
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active
url_temp=[]
url_final=[]

    
    
def get_object_url(bucket_name, file_name):
    # # Initialize the S3 client
    # s3_client = boto3.client('s3')

    # # Generate the object URL
    # expiration = datetime.now() + timedelta(days=3650)
    # object_url = s3_client.generate_presigned_url(
    #     'get_object',
    #     Params={'Bucket': bucket_name, 'Key': file_name},
    #     ExpiresIn=expiration
    # )

    # return object_url
    # Construct the object URL
    encoded_file_name = urllib.parse.quote(file_name)
    object_url = f"https://{bucket_name}.s3.amazonaws.com/{encoded_file_name}"
    return object_url

# if __name__ == "__main__":
#     # Replace 'your-bucket-name' with your bucket's name
    


bucket_name = 'uniqusai-gpt-prod'
try:
    for row in sheet.iter_rows(values_only=True):
        # print(row[0])
        object_url=get_object_url(bucket_name, 'big4/deloitte/'+row[0])
        # print(row[0],object_url)
        url_temp=[row[0],object_url]
        url_final.append(url_temp)
        write_to_excel(url_final)
except:
    write_to_excel(url_final)
    
print(url_final)
#     # List of file names
#     file_names = ['file1.txt', 'file2.jpg', 'file3.pdf']  # Add your file names

#     for file_name in file_names:
#         object_url = get_object_url(bucket_name, 'big4/deloitte/'+file_name)
#         print(f"Object URL for '{file_name}': {object_url}")
