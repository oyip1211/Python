import time
import requests
import urllib
from bs4 import BeautifulSoup

# TODO: Implement the continue_crawl function described above
def continue_crawl(search_history, target_url, max_steps=25):
    history_entry_count = len(search_history)
    
    if search_history[-1] == target_url:
        print(search_history[-1])
        print('Target URL reached.')
        return False
    
    if history_entry_count > max_steps:
        print(search_history[-1])
        print('Too many pages traversed.')
        return False
        
    for link in search_history[0:(history_entry_count-1)]:
        if link == search_history[-1]:
            print(link)
            print('Cycle discovered.')
            return False
    
    return True

def find_first_link(url):
    # get the HTML from "url", use the requests library
    r = requests.get(url)

    # feed the HTML into Beautiful Soup
    soup = BeautifulSoup(r.text, 'html.parser')

    # find the first link in the article
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    first_relative_link = None
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_relative_link = element.find("a", recursive=False).get('href')
            break

    # return the first link as a string, or return None if there is no link
    if not first_relative_link:
        return

    return urllib.parse.urljoin('https://en.wikipedia.org/', first_relative_link)

start_url = 'https://en.wikipedia.org/wiki/Osaka'
target_url = 'https://en.wikipedia.org/wiki/Philosophy'
article_chain = [start_url]

while continue_crawl(article_chain, target_url, 50): 
    # download html of last article in article_chain
    # find the first link in that html
    print(article_chain[-1])
    first_link = find_first_link(article_chain[-1])

    # add the first link to article_chain
    article_chain.append(first_link)

    # delay for about two seconds
    time.sleep(2)