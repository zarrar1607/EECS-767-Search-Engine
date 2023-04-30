'''
Author 1: Vamsi 
Author 2: Zarrar
All is self hand coded
'''
'''
Preparing the documents
Create a Term-Document Matrix with TF-IDF weighting
Calculate the similarities between query and documents using Cosine Similarity
Retrieve the articles that have the highest similarity on it.
'''
from lib.data_handler import *
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
#dontVisit=[]
#Document processing and indexing
#vector space model
#Niche crawler
#query interface
#term proximity scoring

#import requests
#from bs4 import BeautifulSoup

# get_links from a url
# Niche crawl
# Process Robots
# Crawler on  URL Frontier
# Get_content from Collected Data
# Build an Index
# Save the Data that was created on parsing earlier
# Load Data
# search -> Querry

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

processRobots('https://www.ziprecruiter.com/')
#print(f"Links:\n\n{getLinks('https://www.ziprecruiter.com/jobs-search')}")





