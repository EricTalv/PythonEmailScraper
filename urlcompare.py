

urls = {"facebook.com", "vikipedia", "wikipedia"}

with open('blocked_sites.txt','r') as blocked_sites:
   readlines = blocked_sites.readlines()
   for row in readlines:
      print(row)
