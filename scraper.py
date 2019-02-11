# OBJECTIVE: Fetch emails from any given link
'''

Our objective is to fetch emails from any given link
BUT also to fetch any emails from the links we find
on the First link.

Picture:

SCRAPER <- Feed it a link
   |
   ▼
1.Scan for more <a> links
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


'''
