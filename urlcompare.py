

urls = {'facebook.com', 'youtube.com', 'gold'}

# Open blocked sites list
with open('blocked_sites.txt','r') as blocked_sites:
   # Read all line from file
   blocked = blocked_sites.readlines()
   # Compare checks
   ## For each URL in URLS
   for url in urls:
      ## and For each BLOCKER in BLOCKED
      for blocker in blocked:
         ## IF URL is in BLOCKER
          if blocker in url:
               print("[M]URL:{url} = BLOCKER:{blocker}".format(url=url,
                                                               blocker=blocker))
          else:
               print("[N]URL:{url} | BLOCKER:{blocker}".format(url=url,
                                                               blocker=blocker))
     
         # If URLS Contains ITEM in BLOCKED
           # Remove ITEM

         
      # check if URLS has any BLOCKED urls
      # Remove the URLS that are TRUE

