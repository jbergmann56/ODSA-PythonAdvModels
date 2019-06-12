import json
import requests  #GET/POST/PUT API requests
from contextlib import closing  #utilities for common tasks involving the "with" statement.
from bs4 import BeautifulSoup #BeautifulSoup4 - HTML Web Scraping #Scrapy
#more info on bs4:  https://realpython.com/python-web-scraping-practical-introduction//

#get json file from web API 
def API_get():
    #set url for json request, then obtain json response/payload
    view_url = 'https://jsonplaceholder.typicode.com/todos'
    myResponse = requests.get(view_url)
    #print (myResponse.status_code)
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


#Web Scrape experimentation - https://realpython.com/blog/
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_response(resp):
                print('http request successful')
                return resp.content
            else:
                return None

    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)



#API Call/Put function experimentation
#data = API_get()
#print(data) #Print all dict entries in list
#print("Print the title of the 10th entry in returned dictionary: {}".format(data[10]['title']))
#status = API_put(data)  #"put" data using API class
#print(status)

#Web Scrape experimentation - https://realpython.com/python-web-scraping-practical-introduction/
raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
print(len(raw_html)) #if > 0, then successful
#using BeautifulSoap to scrape web page
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('li')): #find all list elements
        print(i, li.text)
