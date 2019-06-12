#https://www.scrapehero.com/scrape-yahoo-finance-stock-market-data/
#Construct the URL of the search results page from Yahoo Finance. 
#   For example, here is the one for Apple-http://finance.yahoo.com/quote/AAPL?p=AAPL
#Step 1) Download HTML of the search result page using Python Requests
#Step 2) Inspect Data Source via web browser (IE) and Python (Print, BS4 Lib)
#Step 3) Parse the page using BS4 HTML Parser + HTML Tag Information
#Step 4) Save the data for Storage - CSV & JSON files.

import requests  #GET/POST/PUT API requests
from contextlib import closing  #utilities for common tasks involving the "with" statement.
from bs4 import BeautifulSoup #BeautifulSoup4 - HTML Web Scraping #Scrapy
import csv #write stock information to csv file
import json #write stock informaton to json file, for future API use
#more info on bs4:  https://realpython.com/python-web-scraping-practical-introduction//

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

#Web Scrape - bloomberg stock market data - S&P 500 example:  https://www.bloomberg.com/quote/SPX:IND
raw_html = simple_get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')

#using BeautifulSoap to scrape and inspect web page
html = BeautifulSoup(raw_html, 'html.parser')
#print(html.prettify())

# Take out the <div> of name and get the stock's value
stock_date = html.findAll("td", attrs={"class": "Py(10px) Ta(start) Pend(10px)"})
#print(stock_date)

#iterate through elements to get stock dates
stock_date = []
for i, text in enumerate(html.findAll("td", attrs={"class": "Py(10px) Ta(start) Pend(10px)"})):
    stock_date.insert(i,text.span.string)
print(stock_date)

#create list to store other stock data
stock_data = []
for i, text in enumerate(html.findAll("td", attrs={"class": "Py(10px) Pstart(10px)"})):
    stock_data.insert(i,text.span.string)
print(stock_data)

#combine date and stock information into dictionary data structure
i = 0
stock_info = {}
for i in range(len(stock_date)-1):  #get stock info for every day
    stock_info[i] = {"date": stock_date[i], "open": stock_data[(i*6)+0], "close": stock_data[(i*6)+3], "volume": stock_data[(i*6)+5]}
    print(stock_info[i])

#export stock information to csv
i = 0
with open('C:\\Python\\Data\\stock_hist.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, stock_info[i].keys(), lineterminator = '\n')
    w.writeheader() 
    while(i<len(stock_info)):
        w.writerow(stock_info[i])
        i += 1

#export stock information to json
jsonarray = json.dumps(stock_info)
print(jsonarray)

#write json file to local drive, for future use
with open('C:\\Python\\Data\\stock_hist.json', 'w') as f:
    json.dump(jsonarray, f)