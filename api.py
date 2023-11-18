import requests


def get_res(file_name,query):
    # API endpoint URL
    url = 'http://15.206.100.201:8000/llm-api/chat'

    # Body parameters as a Python dictionary
    body_params = {
        "type":"ARC",
        "link":"https://uniqusai-gpt-prod.s3.ap-south-1.amazonaws.com/big4/deloitte/deloitte3/"+file_name,
        "query":query
    }

    # Send the POST request with body parameters
    response = requests.post(url, json=body_params)
    final_op=''
    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        final_op=data['response']['message']
    else:
        # Request failed
        print(f"Request failed with status code: {response.status_code}")
        final_op=response.text
    return final_op