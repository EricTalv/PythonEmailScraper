
urls = {'facebook.com', 'youtube.com', 'gold'}
blocker = {'facebook'}

for url in urls:
   if blocker in url:
      urls.remove(url)



print(urls)


