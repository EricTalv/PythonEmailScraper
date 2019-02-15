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
done = False
def animate():
    # Cycle through list
    for c in itertools.cycle(['|', '/', '-', '\\']):
        # if done = true break
        if done:
            break
        # write out 
        sys.stdout.write('\rLoading ' + c)
        # force write all to terminal
        sys.stdout.flush()
        # sleep
        time.sleep(0.1)
    # write out   
    sys.stdout.write('\rDone!     ')

# Thread
t = threading.Thread(target=animate)
t.start()

# Run Request
try:
    res = requests.get(bad_url)
    done = True
    print(res)
    print(done)
except requests.exceptions.HTTPError:
    done = True
    print("[ERROR]")
    print(done)
    sys.exit(0)
finally:
    done = True
print(done)    



