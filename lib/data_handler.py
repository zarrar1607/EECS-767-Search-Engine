from bs4 import BeautifulSoup
import requests
import pandas as pd

disallowed_paths = []

# Grabbing all links in the URL
def getLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = response.content
    job_listings = soup.find_all('tr', {'id': lambda x: x and x.endswith('BR')})
    links = []
    '''
    for link in soup.find_all('a'):
        href = link.get('href')
        try:
            if href.startswith('/') and href not in dontVisit:
                links.append(url+href)
        except AttributeError:
            pass
    '''
    for i in soup.find_all('a'):
        #i['href'] = i['href'] + '?page=all'
        links.append(i)#i['href'])
    return links

def processRobots(url):
    robot = requests.get(url)
    
    soup = BeautifulSoup(robot.text, "html.parser")
    #print(soup)
    # find all disallowed paths
    for line in soup.get_text().split('\n'):
        if line.startswith('Disallow:'):
            path = line.split(': ')[1].strip()
            disallowed_paths.append(path)

    print(disallowed_paths)
    #print(type(soup.text))
    '''
    for line in soup.text.split('\n'):
         if line.startswith("Disallow"):
            dontVisit.append(line.split()[1])
    '''
 