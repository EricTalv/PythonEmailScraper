# PythonWebScraper

An email webscraper to scrape multiple links for a huge array of emails.

# How to use 

All of the scraping is done in `scrape.py`. 

Recommended use:
 + start scraper with `cmd` and run `<root-path>\.scraper.py`

# Theory

*Picture:**
<pre>
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
</pre>
