#url = 'facebook.com'
#blocker = 'facebook'

urls = {'facebook.com', 'youtube.com', 'gold'}
blocked = {'facebook', 'youtube'}

for url in urls:
   for blocker in blocked:
      if blocker in url:
         print("[M]URL:{url} = BLOCKER:{blocker}".format(url=url,
                                                         blocker=blocker))
      else:
        print("[N]URL:{url} | BLOCKER:{blocker}".format(url=url,
                                                        blocker=blocker))
 
