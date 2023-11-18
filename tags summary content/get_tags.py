import ast
import requests
import json
from flask import Flask, jsonify, request
import openpyxl

from write import w_excel


def get_chat_gpt_data(content):


    # Define the endpoint URL
    url = 'https://api.openai.com/v1/chat/completions'

    # Define the body parameters
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Find the tags comma separated and enclosed in single quotes in one line "+ content}],
        "temperature": 0.7
    }
    # Convert the body parameters to JSON
    json_body = json.dumps(body)

    # Set the headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization':'Bearer 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'
    }

    # Make the POST request with the body parameters
    response = requests.post(url, headers=headers, data=json_body)
    if response.status_code == 200:
        data = response.json()
        tags=data["choices"][0]["message"]['content']
        temp_tags=tags.split(",")
        tagArr=[]
        for s in temp_tags:
            # print()
            tagArr.append(str(s).replace("'",''))
        # print(summary,data['usage']['total_tokens'])
    # print('tagArr',tagArr,'\n','tags',tags)
    return [tagArr,tags]


# get_chat_gpt_data('''Based on the provided text, it appears to be discussing the issue of trust in various institutions, specifically focusing on business, government, NGOs (non-governmental organizations), and media. The text mentions that trust is granted based on two attributes: competence and ethical behavior.
 
#  In terms of competence, business is seen as the most competent institution, with a significant 54-point edge over government in delivering on promises. However, none of the institutions are perceived as both competent and ethical.
 
#  When it comes to ethical behavior, NGOs are seen as the leaders, with a 31-point gap over government and a 25-point gap over business. Both government and media are perceived as both incompetent and unethical.
 
#  The text also mentions the expectations people have from businesses, such as paying decent wages and providing retraining for workers whose jobs are threatened by automation. However, it states that less than a third of people trust that businesses will fulfill these expectations.
 
#  Overall, the text highlights the importance of trust in institutions and the current lack of trust in both government and business. It suggests that businesses need the help of government to address certain societal issues and regain trust.''')



# Specify the file path of your Excel file
file_path = 'content.xlsx'

# Load the Excel workbook
workbook = openpyxl.load_workbook(file_path)
temp_arr=[]
arr=[]
# Choose a specific sheet to read (by default, it selects the first sheet)
sheet = workbook.active
try:
    for r,row in enumerate(sheet.iter_rows(values_only=True)):
            if row[0]==None:
                break
            else:
                d=get_chat_gpt_data(row[0])
                tagarr_final=d[0]
                tags_final=d[1]
            temp_arr=[row[0],tags_final,str(tagarr_final)]
            print(r)
            arr.append(temp_arr)
            temp_arr=[]
    w_excel(arr)
except:
        print(r)
        
        w_excel(arr)
workbook.close()
    
        