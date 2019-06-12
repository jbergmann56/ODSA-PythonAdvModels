#Purpose: Basic REST API GET & Put Request Example
#Training Website:  https://jsonplaceholder.typicode.com
import json
import requests  #GET/POST/PUT API requests
from contextlib import closing  #utilities for common tasks involving the "with" statement.

#get json file from web API 
def API_get():
    #Step 1 - Identify Resource: set url for json request
    view_url = 'https://jsonplaceholder.typicode.com/todos'
    #Step 2&3 - Access Endpoints (GET) and Methods (https://jsonplaceholder.typicode.com)
    #Step 4 - obtain json response/payload via Requests Library, then return parsed response (JSON to Dictionary)
    myResponse = requests.get(view_url)
    print (myResponse.status_code)
    # For successful API call, response code will be 200 (OK)
    if(myResponse.ok):
        # Loads (Load String) takes a Json file and converts into python data structure 
        # (dict or list, depending on JSON structure and number of records returned
        jData = myResponse.content 
        # Loading the response data into a dict variable
        jData = json.loads(jData) 
        print("The API Get Request Was Successful")
        print("\n")
        return jData
        
    else:
        # If response code is not ok (200), print the resulting http error code with description
        print('API Error')
        return ''

def API_put(data):
    view_url = 'https://jsonplaceholder.typicode.com/posts/1'
    print('API Put - convert dict data structure to json') 
    json2 = json.dumps(data) 
    myResponse = requests.put(view_url, data=json2)
    print (myResponse.status_code)
    # For successful API call, response code will be 200 (OK)
    if(myResponse.status_code == 200):
        return "The API Put Request Was Successful"
    else:
        #If response code is not ok (200), print the resulting http error code with description
        return "The API Put Request Was Successful"

#Step 5: Recieve Response and Parse Data
#API Call/Put function experimentation
data = API_get()
print(data) #Step 5: Print all dict entries in list
print("Print the title of the 10th entry in returned dictionary: {}".format(data[10]['title']))
status = API_put(data)  #"put" data using API class
print(status)

