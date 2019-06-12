import requests  #GET/POST/PUT API requests
from contextlib import closing  #utilities for common tasks involving the "with" statement.
from bs4 import BeautifulSoup #BeautifulSoup4 - HTML Web Scraping #Scrapy
#more info on bs4:  https://realpython.com/python-web-scraping-practical-introduction//


#Web Scrape experimentation - https://realpython.com/blog/
#Step 1 - Make Web Request
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


#Step 1 - Obtain HTTP Web Request
raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
#Step 2: Inspect Data Source
print(len(raw_html)) #if > 0, then successful

#using BeautifulSoap to scrape web page
html = BeautifulSoup(raw_html, 'html.parser')

#print parsed html file with easier-to-read "pretty" output
print(html.prettify()) 

#Step 3) Reangling/Transforming HTML Elements
#create python dictionary of top mathematicatians and ranks, found in list (li) tags
math_men = {}
for i, text in enumerate(html.find_all('li')):
    math_men[i+1] = {"rank": i+1, "name": text.a.string}

#print the 34th best mathematician
print(math_men[34])

#print all mathematicians
print(math_men)
