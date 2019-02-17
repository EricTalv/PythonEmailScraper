

urls = {"facebook.com", "vikipedia", "wikipedia", "gold"}

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
         if url in blocker:
            print("URL:{url} | BLOCKER:{blocker}".format(url=url,
                                                         blocker=blocker))
         else:
            print("no match")
     
         # If URLS Contains ITEM in BLOCKED
           # Remove ITEM

         
      # check if URLS has any BLOCKED urls
      # Remove the URLS that are TRUE

