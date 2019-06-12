#Purpose: REST API Example using Stored stock market data, along with Google Fusion Tables
import json
import csv
import requests  #GET/POST/PUT API requests
from contextlib import closing  #utilities for common tasks involving the "with" statement.

#Step 1 - Identify Resource: set url for json request
view_url = 'https://accounts.google.com/o/oauth2/token'
#Step 2 & 3 - Identify Endpoints, Methods and Set request parameters
client_id='615800458288-5fktbjo6kmu18bpgl18glnj2l12mvg8i.apps.googleusercontent.com'
client_secret='QowLGwV4wueqHpV_t1sotQVh'
refresh_token = '1/vz7AvnbcT05ZJI-SQcFACqhaif9hXCfeuTM8n1DI12E'
refresh_body = "refresh_token=" + refresh_token + '&client_id=' + client_id + '&client_secret=' + client_secret + '&grant_type=refresh_token'

#Step 1-3) Google Fusion Tables OAuth keys
def API_POST_OAuth():
    #set url for json request, then obtain json response/payload
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    myResponse = requests.post(view_url, data=refresh_body, headers=headers)
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

#Step 1-3) Google Fusion Table - Replace
def API_POST_Data(access_token, table_id, data):
    data_view_url = "https://www.googleapis.com/upload/fusiontables/v2/tables/" + table_id + '/replace?&access_token=' + access_token + '&isStrict=false'
    headers = {'Content-type': 'application/octet-stream'}
    #create post response body - comma seperated string of all obs
    print(range(len(data)))
    print('iterate list')
    data2 = ""
    for i in range(len(data)):
        dict1 = data[i]
        dict2 = dict1['date'].replace(",","") + ', ' + dict1['open'] + ', ' + dict1['close'] + ', ' + dict1['volume'].replace(",","") + '\n'
        data2 = data2 + dict2  
    myResponse = requests.post(data_view_url, data=data2, headers=headers)
    print (myResponse.status_code)
    # For successful API call, response code will be 200 (OK)
    if(myResponse.status_code == 200):
        return "The API Post Request Was Successful"
    else:
        #If response code is not ok (200), print the resulting http error code with description
        return "The API Post Request Was Not Successful"

#step 4 - create request data structure from csv file, to replace data in the "OSDA Stock History" google fusion table
#https://fusiontables.google.com/data?docid=1a8EPfomscPkMYksFrlGoyU4utoT0QdLCpH9tySDP#rows:id=1 
reader = csv.DictReader(open('C:\\Python\\Data\\stock_hist.csv'))
stock_data = list(reader)
print(type(stock_data)) #list of dictionaries
print(stock_data[0])
#Obtain Google Fusion OAuth token 
data = API_POST_OAuth()
access_token = data['access_token']

#Put data in google fusion table
table_id = '1a8EPfomscPkMYksFrlGoyU4utoT0QdLCpH9tySDP'
#convert stock_data to json fiel
status = API_POST_Data(access_token, table_id, stock_data)  #"put" data using API class
print(status)

