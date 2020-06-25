# PythonWebScraper

This is an email webscraper to scrape multiple links for a huge array of emails.

# How to use 

All of the scraping is done in `scrape.py`. 

Recommended use
 + start scraper with `cmd` and run `<root-path>\.scraper.py`

#### blocked_emails.txt

You might find some emails re-occuring, or maybe you just need to block some "strings", yeah this isnt only for blocking emails but you can also block any type of string necessary

#### blocked_sites.txt

Some sites might be a bit too bulky to crawl thus it will stall the scraper, or some sites have a "gotcha" feature that is meant to stall the scraper, best to block these sites here. 

# Install modules:

pip install:
 + requests
 + bs4 
 + colorama
 + lxml
 

# Theory

*Picture:**
<pre>
SCRAPER <- Feed it a link
   |
   ▼
1.Scan for more links
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
4.Repeate til no new links or emails are found
</pre>
