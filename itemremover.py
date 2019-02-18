
urls = {'facebook.com', 'youtube.com', 'gold'}
blocked = {'facebook'}

for url in urls:
   for blocker in blocked:      
      if blocker in url:
         urls.remove(url)
         print('removed: ' + url)
      else:
         print('no item')


