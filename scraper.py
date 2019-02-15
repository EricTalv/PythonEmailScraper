# Import libraries
import re
import requests
import requests.exceptions
import csv
import signal
import sys
import itertools
import threading
import time
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
from colorama import *
init()

# starting url. replace google with your own url.
# starting_url = 'https://erictalv.github.io./' #'https://www.neti.ee/cgi-bin/teema/ARI/Byrooteenused/'

# UNCOMMENT THIS ON PRODUCTION
print(Back.BLUE + "|~~~~Email Scraper v2~~~~|" )
starting_url = input("Enter Website Link to Scrape: ")
print("Starting scraper.." + Back.BLACK)

# a queue of urls to be crawled
unprocessed_urls = deque([starting_url])

# set of already crawled urls for email
processed_urls = set()

# a set of fetched emails
emails = set()

# A fancy bar
def Bar(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

# CSV Writer function
# CSV Writer function
def write_csv(dirpath, file_name, collection):
    print("[WRTIER]Loading..")
    # Open writer, set file_name and path
    def writer():
        print("[WRITER]Pass Writer")
        # Pass email_file to writer
        writer = csv.writer(email_file,
                            delimiter=' ',
                            quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)

        print("[WRITER]Writing through collections:")
        # For every item inside the collection write a row
        for row in collection:
            print(row)
            writer.writerow([row])
        print("[WRITER]Done")    

    # check Dir Path
    if len(dirpath) is 0:
         with open(file_name + '.csv', 'w') as email_file:
            writer()         
    else:
        with open(dirpath + '\\' + file_name + '.csv', 'w') as email_file:
            writer()

# Create End_Scene
def end_scene():
    print(Back.GREEN + Bar('=', 50) + Back.BLACK)
    print("[[Session Stopped]]")
    print("Emails Found:")
    print(Fore.CYAN)
    print("\n".join(emails))
    print(Fore.WHITE)
    print(Back.GREEN + Bar('=', 50) + Back.BLACK)
    
    session_choice = input("Save emails as .CSV?[Y/]").upper()
    if session_choice == 'Y':
        file_path = input("Insert Path Or Leave Empty |Saves to root folder: ")
            
        # Ask For Name
        csv_name = input("Insert Name or Leave Empty |Generates name from URL: ")
        if len(csv_name) is 0:
            gen_name = starting_url.split("//")[-1].split("/")[0]
            # Ask For File Path           
            write_csv(file_path, gen_name, emails)
        else:
            # Ask For File Path
            write_csv(file_path, csv_name, emails)            
    else:
         print("Not Saved | Session Ended.")
         sys.exit()

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
    
         
# process urls one by one from unprocessed_url queue until queue is empty
while len(unprocessed_urls):
    # Thread
    t = threading.Thread(target=animate)
    

    # move next url from the queue to the set of processed urls
    url = unprocessed_urls.popleft()
    processed_urls.add(url)

    # extract base url to resolve relative links
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    # get url's content
    print(Fore.CYAN + "Crawling URL %s" % url + Fore.WHITE) 
    try:
        t.start()
        response = requests.get(url, timeout=3)
        done = True
    except requests.exceptions.ConnectionError as e:
        print("\n[ERROR]Connection Error:")
        print(e)
        continue
    except requests.Timeout as e:   
        print("\n[ERROR]Connection Timeout:")
        print(e)
        continue
    except requests.HTTPError as e:   
        print("\n[ERROR]HTTP Error:")
        print(e)
        continue
    except requests.RequestException as e:   
        print("\n[ERROR]General Error:")
        print(e)
        continue    
        # Check for CTRL+C interruption
    except KeyboardInterrupt:
        if len(emails) is 0:
            print("No emails have been collected |Crawling Ended")
        else:
            end_scene()
    finally:
        done = True
    

    # extract all email addresses and add them into the resulting set
    # You may edit the regular expression as per your requirement
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)
    
    if len(new_emails) is 0:
        print(Back.RED)        
        print("No emails found")
        print(Back.BLACK)
    else:
        print(Fore.GREEN) 
        print(new_emails)
        print("Email Count: ", len(emails))
        print(Fore.WHITE)
    
    # create a beutiful soup for the html document
    soup = BeautifulSoup(response.text, 'lxml')

    # Once this document is parsed and processed, now find and process all the anchors i.e. linked urls in this document
    for anchor in soup.find_all("a"):
        # extract link url from the anchor
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        # resolve relative links (starting with /)
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        # add the new url to the queue if it was not in unprocessed list nor in processed list yet
        if not link in unprocessed_urls and not link in processed_urls:
            unprocessed_urls.append(link)

if len(emails) is 0:
    print("No emails have been collected |Crawling Ended")
else:
    end_scene()



