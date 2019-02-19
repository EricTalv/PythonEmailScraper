from timeit import default_timer as timer

urls = ['facebook.com', 'youtube.com', 'gold']
blocked = ['facebook', 'netflix','youtube']

def remover():      
   for url in urls:
      for blocker in blocked:      
         if blocker in url:
            urls.remove(url)
            print('removed: ' + url)



