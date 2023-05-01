import re
import nltk
import string
import requests
import pandas as pd
from bs4 import BeautifulSoup
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize


disallowed_paths = []

# Checking Robot
def check_robots(url):
    robots_url = url+'/robots.txt'
    response = requests.get(robots_url)

    robots_txt = response.text
    soup = BeautifulSoup(robots_txt, "lxml")
    #print(soup)
    
    # find all disallowed paths
    for line in soup.get_text().split('\n'):
        if line.startswith('Disallow:'):
            path = line.split(': ')[1].strip()
            disallowed_paths.append(path)

    #print(f'Disallowed Path: \n{disallowed_paths}')
    

# Grabbing all links in the URL
def get_links(url):
    # get the webpage using requests
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'Error fetching {url}: {e}')
        pass
    # parse the webpage with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    # find all links in the webpage
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            if (href.startswith('/co/'))and not href.startswith('#') and href not in disallowed_paths:
                print(url+href)
                links.append(url+href)
        except AttributeError:
            pass
    return links

def get_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text


def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text)
    
    # Convert to lowercase
    tokens = [token.lower() for token in tokens]

    # Define stopwords and stemmer
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    
    # Remove stop words and punctuation
    tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
    
    # Lem words
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    '''
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    tagged_words = pos_tag(words)
    tagged_words = [(word, tag) for word, tag in tagged_words if tag.startswith('N') or tag.startswith('V') or tag.startswith('J') or tag.startswith('R')]
    doc = ' '.join([word for word, tag in tagged_words])
    '''
    # Return preprocessed text as a single string
    return ' '.join(tokens)


def save_as_text(text_list, file_name):
    with open(f'./data/{file_name}.txt', 'w') as f:
        f.write('\n'.join(text_list))

def load_from_txt(file_name):
    with open(f'./data/{file_name}.txt', 'r') as f:
        text_list = f.read().splitlines()
    return text_list

def save_table(df, file_name):
    df.to_csv(f'./data/{file_name}.csv')

def load_table(file_name):
    return pd.read_csv(f'./data/{file_name}.csv', index_col=0)
