from bs4 import BeautifulSoup
import requests
import pandas as pd

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
    response = requests.get(url)
    # parse the webpage with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    links = []
    # find all links in the webpage
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            if href.startswith('/') and not href.startswith('#') and href not in disallowed_paths:
                #print(url+href)
                links.append(href)
        except AttributeError:
            pass

    return links

