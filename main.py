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
from lib.indexer import *
from lib.query_processor import *
from collections import deque
#import time
#from libs.saveLoad import *
#from bs4 import BeautifulSoup
#import xml.etree.ElementTree as ET
#import requests
#import time


# Document processing and indexing - Done
# vector space model - Done
# Niche crawler - Done
# query interface - Done
# term proximity scoring - Done

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
    # Get all the links on the current/seed page
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
#niche_crawl('https://www.ziprecruiter.com', 1)
#url = 'https://www.ziprecruiter.com'
#url = 'https://www.ziprecruiter.com/co/ADP/Jobs'
#url = 'https://www.ziprecruiter.com/c/Nike/Job/Store-Associate-Seasonal-Kansas-City,-KS/-in-Kansas-City,KS?jid=775c0e7a3b493b0a&lvk=U9n257hnuDREgl05MkIxTA.--Mu_-isTxg'
#niche_crawl(url=url, max_depth= 1)
#print(f"Links:\n\n{url_frontier}")
#print(f"\n\nContent:\n {get_content(url=url)}")
# code for scrapping from the links 

'''

import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

job_names = []
job_links = []
documents = {}
preproc_docs = {}
#preproc_docs_demo = []
r = 0
  
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text

def preprocess_doc(doc):
    doc = doc.lower()
    words = word_tokenize(doc)
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w) for w in words]
    tagged_words = pos_tag(words)
    tagged_words = [(word, tag) for word, tag in tagged_words if tag.startswith('N') or tag.startswith('V') or tag.startswith('J') or tag.startswith('R')]
    doc = ' '.join([word for word, tag in tagged_words])
    return doc
### crawling the employment.ku.edu website ###
response = requests.get('https://employment.ku.edu/jobs')
soup = BeautifulSoup(response.content, 'html.parser')

job_listings = soup.find_all('tr', {'id': lambda x: x and x.endswith('BR')})
for listing in job_listings:
    job_name_elem = listing.find('td', {'class': 'job-name-row'})
    if job_name_elem is not None:
        job_name = job_name_elem.text.strip() 
        job_link = "https://employment.ku.edu" + job_name_elem.find('a').get('href')
    else:
        job_name = ''
        job_link = ''
    job_links.append(job_link) 
    job_names.append(job_name)
#print(job_links)

for i in job_links:
    text = extract_text_from_url(i)
    documents[i]=text

for i in job_links:
    doc = documents[i]
    preproc_docs[i] = str(job_names[r])+" "+preprocess_doc(doc)
    print(preproc_docs[i])
    r = r+1


documents = preproc_docs

for key, value in documents.items():
    documents[key] = preprocess_text(value)

inverted_index = build_inverted_index(documents)
print(f'inverted_index:\n {inverted_index.head()}')

tf_idf_table = create_tf_idf(inverted_index)
print(f'tf_idf_table:\n {tf_idf_table.head()}')

'''

# Sample query
query = "Desk Job"
documents = pd.read_csv('./data/document.csv')
tfidf_table = pd.read_csv('./data/tf_idf.csv', index_col=0)

print(documents.head())
print(tfidf_table)


# Perform the query search
search_results = search_query(query)

# Print the search results
save_table(pd.DataFrame(search_results).head(5),'result')
print(pd.DataFrame(search_results).head(5))

