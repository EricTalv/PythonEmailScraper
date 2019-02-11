# OBJECTIVE: Fetch html data from any given link
# METHOD: Inspect-Element

# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Lets get the URL as client input
#link = input("Insert a Link: ")
link = 'https://veebisekretar.ee/'

# Open url and store it 
html = urlopen(link)

soup = BeautifulSoup(html, 'html.parser')

print(soup)
