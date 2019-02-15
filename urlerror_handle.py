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
    res = requests.get(bad_url, timeout=0.001)
    print(res)
except requests.exceptions.ConnectionError as e:
    print("\n[ERROR]Connection Error:")
    print(e)
except requests.TooManyRedirects as e:   
    print("\n[ERROR]Too many Redirects:")
    print(e)
except requests.Timeout as e:   
    print("\n[ERROR]Connection Timeout:")
    print(e)
except requests.HTTPError as e:   
    print("\n[ERROR]")
    print(e)
    sys.exit(1)
except requests.RequestException as e:   
    print("\n[ERROR]")
    print(e)
    sys.exit(1)    
finally:
    done = True
    


