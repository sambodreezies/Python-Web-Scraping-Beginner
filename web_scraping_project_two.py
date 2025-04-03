print("\033c")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


URL = 'https://pythonjobs.github.io/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_ = 'job_list')
job_cards = results.find_all("div", class_ = 'job')

count = 1
for job in job_cards:
    
    title_element = job.find('h1').get_text(strip = True)
    location_element = job.find('span').get_text(strip = True)
    description_element = job.find('p').get_text(strip = True)
    spans = job.find_all(class_ = 'info')
    if spans:
        posted_element = spans[1].get_text(strip = True)
        company_element = spans[3].get_text(strip = True)

    print(f"{count}. {title_element}")
    print()
    print(f"Date Posted: {posted_element}")
    print(f"Location: {location_element}")
    print(f"Company: {company_element}")
    print()
    print(f"Description: \n{description_element}")
    print('\n')
    count += 1
