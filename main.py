'''
Author 1: Vamsi 
Author 2: Zarrar
Every caharacter is self hand coded
'''
'''
Preparing the documents
Create a Term-Document Matrix with TF-IDF weighting
Calculate the similarities between query and documents using Cosine Similarity
Retrieve the articles that have the highest similarity on it.
'''
from lib.data_handler import *
from collections import deque
#from libs.search import *
#from libs.indexing import *
#import time
#from libs.saveLoad import *
#from bs4 import BeautifulSoup
#import xml.etree.ElementTree as ET
#import requests
#import time

#processedData = []
#originaldata=[]
#linker = []
#dataWPara={}
#urlsfrontier=[]
#uniquewords = []
#df = []
#robots=[]
#dontVisit=[] - Done
#Document processing and indexing
#vector space model
#Niche crawler
#query interface
#term proximity scoring

#import requests
#from bs4 import BeautifulSoup

# get_links from a url - Done
# Niche crawl
# Process Robots
# Crawler on  URL Frontier
# Get_content from Collected Data
# Build an Index
# Save the Data that was created on parsing earlier
# Load Data
# search -> Querry
url_frontier = []
url_visited = set()
def niche_crawl(url, max_depth=1):
    if not max_depth:
        return
    
    if url not in url_visited:
        url_frontier.append(url)
    
    links = get_links(url=url)
    
    for link in links:
        if link in url_visited:
            continue
        url_visited.add(link)
        if link not in url_frontier:
            url_frontier.append(link)
        niche_crawl(url=link, max_depth=max_depth-1)
    

'''
inp = input('>> ')
while inp !='launch':
    if inp == 'start':
        print('starting')
        p = time.time()
        processRobots()
        niche_crawl('https://bbc.com/sport', 1)
        crawl()
        indexer()
        print('total execution time ', str(time.time()-p))
    elif inp == 'save':
        print('saving...')
        saveData()
        print('saved')
    elif inp == 'load':
        print('loading...')
        loadData()
        print('loaded')
    elif inp =='robot':
        processRobots()
    else:
        print('unknown command')
    inp = input('>> ')
'''
# saveLoad()
# search('vegetarian recipe burst flavour plus information substitution and food')

#check_robots('https://www.ziprecruiter.com')
niche_crawl('https://www.ziprecruiter.com', 1)
print(f"Links:\n\n{url_frontier}")




