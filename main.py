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
# Define an empty list to store the URLs to visit
url_frontier = []

# Define a set to store the URLs that have already been visited
url_visited = set()

# Define the niche_crawl function that takes a URL and a maximum depth as arguments
def niche_crawl(url, max_depth=1):
    
    # Check if we have reached the maximum depth, and return if so
    if not max_depth:
        return
    
    # Check if the URL has not been visited before, and add it to the frontier if so
    if url not in url_visited:
        url_frontier.append(url)
    
    # Get all the links on the current page
    links = get_links(url=url)
    
    # Iterate over the links
    for link in links:
        
        # Check if the link has already been visited, and continue to the next link if so
        if link in url_visited:
            continue
        
        # Add the link to the visited set
        url_visited.add(link)
        
        # Add the link to the frontier if it hasn't already been added
        if link not in url_frontier:
            url_frontier.append(link)
    
        # Recursively call the niche_crawl function with the new link and a depth of one less than the current depth
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




