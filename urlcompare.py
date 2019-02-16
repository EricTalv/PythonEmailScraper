

urls = {"facebook.com", "vikipedia", "wikipedia"}

with open('blocked_sites.txt','r') as blocked_sites:
   lines = blocked_sites.readlines()
   for row in lines:
      print(row)
