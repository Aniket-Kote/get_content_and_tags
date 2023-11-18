from datetime import datetime
import time
import openpyxl

from api import get_res
from write import w_excel

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%Y-%m-%d")


# Specify the file path of your Excel file
file_path = 'Big 4.xlsx'

# Load the Excel workbook
workbook = openpyxl.load_workbook(file_path)

# Choose a specific sheet to read (by default, it selects the first sheet)
sheet = workbook.active
temp_arr=[]
arr=[]
# Read data from the selected sheet
try:
    for row in sheet.iter_rows(values_only=True):
        if row[0]==None:
            break
        else:
            print(row[0].strip())
            mode="OFFLINE"
            publishedOn=str(dt_string)
            refreshedOn=str(dt_string)
            source="https://uniqusai-gpt-prod.s3.ap-south-1.amazonaws.com/big4/ey/"+row[0].strip()
            priority=2
            summary_data=get_res(row[0].strip(),"Act as Accounting expert, write a summary 300 words max, do not mention you are an AI language model.")
            content_data=get_res(row[0].strip(),"Act as Accounting expert, get main content and insights from this text, ignore content from other article and ad references that this text might be having, do not mention you are an AI language model.")
            tags="IFRS,Bare Text,IAS,IAS 24 Related Party Disclosures.pdf,IFRS,Guidance Material,2022,IFRS Part B (Accompanying Guidance),IASs"
            tagArr=[ "IFRS", "Bare Text", "IAS", "IAS 24 Related Party Disclosures.pdf", "IFRS", "Guidance Material", "2022", "IFRS Part B (Accompanying Guidance)", "IASs"]
            title=row[0].strip()
            status="active"
            link="https://uniqusai-gpt-prod.s3.ap-south-1.amazonaws.com/big4/ey/"+row[0].strip()
            fileMeta={
                "name":row[0],
                "mime":"application/pdf",
                "size":'',
                "extn":"pdf",
                "pages":''
            }
        
        
        # temp_arr=[row[0],row[1],summary_data,content_data]
        temp_arr=[mode,publishedOn,refreshedOn,source,str(priority),content_data,summary_data,tags,str(tagArr),title,status,link,str(fileMeta)]
        arr.append(temp_arr)
        temp_arr=[]
        time.sleep(1)
        # print(data)
    # Close the workbook after reading
    arr_headings=['mode','publishedOn','refreshedOn','source','priority','content','summary','tags','tagArr','title','status','link','fileMeta']
    arr.insert(0,arr_headings)
    w_excel(arr)
except:
    arr_headings=['mode','publishedOn','refreshedOn','source','priority','content','summary','tags','tagArr','title','status','link','fileMeta']
    arr.insert(0,arr_headings)
    w_excel(arr)
workbook.close()
