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

        start = time.time()
        for s in int(start):
            sys.stdout.write([str(s)])
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
    res = requests.get(bad_url, timeout=0.001)
    done = True
    print(res)
except requests.exceptions.ConnectionError as err:
    done = True
    print("\n[ERROR]")
    print(err)

finally:
    done = True
    


