# Import libraries
import re
import requests
import requests.exceptions
import csv
import signal
import sys
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

# site_blockers
site_blockers = set(line.strip() for line in open('blocked_sites.txt'))

# email_blockers
email_blockers = set(line.strip() for line in open('blocked_emails.txt'))

# a queue of urls to be crawled
unprocessed_urls = deque([starting_url])

# set of already crawled urls for email
processed_urls = set()

# a set of fetched emails
emails = set()

# KeyboardInterrupt Handler
def signal_handler(sig, frame):
    end_scene()
signal.signal(signal.SIGINT, signal_handler)

# A fancy bar
def Bar(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

# CSV Writer function
# CSV Writer function
def write_csv(dirpath, file_name, collection):
    # Open writer, set file_name and path
    def writer():
        # Pass email_file to writer
        writer = csv.writer(email_file,
                            delimiter=' ',
                            quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
        # For every item inside the collection write a row
        for row in collection:
            print(row)
            writer.writerow([row])

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
    print("[[Session Stopped]]" )
    print("Emails Found:" + str(len(emails)))
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

# process urls one by one from unprocessed_url queue until queue is empty
while len(unprocessed_urls):

    # Remove unwanted items
    unprocessed_urls = deque({url for url in unprocessed_urls if not any(site_blocker in url for site_blocker in site_blockers)})

    # move next url from the queue to the set of processed urls
    newurl = unprocessed_urls.popleft()
    processed_urls.add(newurl)

   
    # extract base url to resolve relative links
    parts = urlsplit(newurl)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    if parts.scheme !='mailto' and parts.scheme !='#':
        path = newurl[:newurl.rfind('/')+1] if '/' in parts.path else newurl
    else:
        continue
    
    # get url's content
    print(Fore.CYAN + "Crawling URL %s" % newurl + Fore.WHITE) 
    try:       
        response = requests.get(newurl, timeout=3)
        done = True
    except requests.exceptions.ConnectionError as e:
        print(Back.RED + "[ERROR]Connection Error:" + Back.BLACK)
        print(Fore.RED)
        print(e)
        print(Fore.WHITE)  
        continue
    except requests.Timeout as e:   
        print(Back.RED + "[ERROR]Connection Error:" + Back.BLACK)
        print(Fore.RED)
        print(e)
        print(Fore.WHITE)   
        continue
    except requests.HTTPError as e:   
        print(Back.RED + "[ERROR]Connection Error:" + Back.BLACK)
        print(Fore.RED)
        print(e)
        print(Fore.WHITE)  
        continue
    except requests.RequestException as e:   
        print(Back.RED + "[ERROR]Connection Error:" + Back.BLACK)
        print(Fore.RED)
        print(e)
        print(Fore.WHITE)    
        continue    
        # Check for CTRL+C interruption
    except KeyboardInterrupt:
        if len(emails) is 0:
            print("No emails have been collected |Crawling Ended")
        else:
            end_scene()
            

    # extract all email addresses and add them into the resulting set
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    # Remove any blocked emails
    new_emails = [email for email in new_emails if not any(email_blocker in email for email_blocker in email_blockers)]
    emails.update(new_emails)

    if len(new_emails) is 0:
        print(Fore.RED)
        print("No emails found")
        print("URLS: {processed}/{unprocessed}".format(processed=str(len(processed_urls)),
                                                       unprocessed=str(len(unprocessed_urls))))
        print("Email Count: ", len(emails))
        print(Fore.WHITE)
    else:
        print(Fore.GREEN) 
        print(new_emails)
        print("Email Count: ", len(emails))
        print("URLS: {processed}/{unprocessed}".format(processed=str(len(processed_urls)),
                                                       unprocessed=str(len(unprocessed_urls))))
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



