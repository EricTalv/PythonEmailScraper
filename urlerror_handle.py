import requests
import itertools
import threading
import time
import sys

# Define URLS
bad_url = 'https://erictalv.git'
good_url = 'https://erictalv.github.io./'
timeout_url = 'ferdida.com'

# Loading Animation
finished = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

# Thread
t = threading.Thread(target=animate)
t.start()

# Run Request
try:
    while finished is False:
        res = requests.get(bad_url)
    finished = True
    print(res)
except requests.exceptions.HTTPError as err:
    finished = True
    print("[ERROR]" + err)


