
urls = ['facebook.com', 'youtube.com', 'gold']
blocked = ['facebook', 'youtube']

for url in urls:
   for blocker in blocked:      
      if blocker in url:
         urls.remove(url)
         print('removed: ' + url)
print(urls)

