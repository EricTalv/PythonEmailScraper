# PythonWebScraper

Another web-scraper to get some tasty emails 

# How to use 

All of the scraping is done in `scrape.py`. 

# Theory

*Picture:**

SCRAPER <- Feed it a link
   |
   ▼
1.Scan for more `<a>` links
  |     |
  |     |
  |     ▼
  |   1.2.Remember the links   
  |                        |
  ▼                        | 
2.Scan the link for Emails |
     |                     |
     ▼                     ▼
3.Take new links and scan them for more emails & links 
  |
  ▼
4.Repeate til no new links or emailes are found