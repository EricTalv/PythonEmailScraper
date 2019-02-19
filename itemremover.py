from timeit import default_timer as timer

processed_urls = set()
unprocessed_urls = {'facebook.com', 'youtube.com', 'gold'}
blockers = {'facebook', 'netflix','youtube'}

def remover():      
   for url in unprocessed_urls:
      for blocker in blockers:      
         if blocker in url:
            processed_urls.add(url)
            print('moved: ' + url)



start = timer()

remover()

end = timer()

print(end - start)
print("P_URLS: ")
print(processed_urls)
print("U_URLS: ")
print(unprocessed_urls)
print("Difference: ")
print(unprocessed_urls.difference(processed_urls))
