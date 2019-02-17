

urls = {'facebook.com', 'youtube.com', 'gold'}

blocked = set(line.strip() for line in open('blocked_sites.txt'))

# Open blocked sites list
#with open('blocked_sites.txt','r') as blocked_sites:  
# For every URL in URLS
for url in urls:
   # For every BLOCKER in BLOCKED_SITES
   for blocker in blocked:
      # If url CONTAINS Blocker
      if blocker in url:
           print("[M]URL:{url} == BLOCKER:{blocker}".format(url=url,
                                                           blocker=blocker))
      else:
           print("[N]URL:{url} || BLOCKER:{blocker}".format(url=url,
                                                           blocker=blocker))
 
