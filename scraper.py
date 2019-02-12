# OBJECTIVE: Fetch html data from any given link
# METHOD: Inspect-Element

# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Lets get the URL as client input
#link = input("Insert a Link: ")
link = 'https://veebisekretar.ee/'

# Open URL request on link 
req = urlopen(link)

# Parse response HTML data 
res = BeautifulSoup(req, 'html.parser')

# Print response data 
print('Success \n', res)
