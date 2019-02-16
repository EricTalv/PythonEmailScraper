#l1 = [1,2,6,8]
#l2 = [2,3,5,8]

urls = set(['facebook',
            'youtube',
            'ikipedia',
            'things i want',
            'ineed',
            'website@com',
            'netflix',
            'wikipedia'])
blocked  = set(['netflix', 'facebook', 'youtube', 'ikipedia'])


if blocked in urls:
   print("found")
