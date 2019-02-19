from timeit import default_timer as timer
from collections import deque

processed_urls = set()
unprocessed_urls = deque(['facebook.com', 'youtube.com', 'gold'])
blockers = ['facebook', 'netflix','youtube']

def remover():      
   for url in unprocessed_urls:
      for blocker in blockers:      
         if blocker in url:
            newurl = unprocessed_urls.popleft()
            processed_urls.add(newurl)
         


start = timer()

remover()

end = timer()

print(end - start)
print("P_URLS: ")
print(processed_urls)
print("U_URLS: ")
print(unprocessed_urls)
#print("Difference: ")
#print(unprocessed_urls.difference(processed_urls))
