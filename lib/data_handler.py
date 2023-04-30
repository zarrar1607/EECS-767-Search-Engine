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
                #print(url+href)
                links.append(url+href)
        except AttributeError:
            pass
    return links



def get_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    content = []
    job_title = soup.find_all('h2')
    para = soup.find_all('p')
    for j in job_title:
        content.append(j.text)
    for p in para:
        if not p.text.lower().startswith('last updated'):
            content.append(p.text)
    return content