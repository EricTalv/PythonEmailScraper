# OBJECTIVE: Fetch html data from any given link
# METHOD: Inspect-Element

# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

from requests import get
from requests.exceptions import RequestException
from contextlib import closing

# Lets get the URL as client input
#link = input("Insert a Link: ")
link = 'https://veebisekretar.ee/'

# Request data Function
def simple_get(url):
   
    # Attempts to get the content at `url` by making an HTTP GET request.
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    # Returns True if the response seems to be HTML, False otherwise.
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def log_error(e):
    # Print any errors
    print(e)


simple_get(link)   
