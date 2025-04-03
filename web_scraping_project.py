print("\033c")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

URL = "https://www.python.org/jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# print(page.text)

results = soup.find(id = 'content')
print(results.prettify())

python_jobs = results.find_all("a", string = lambda text: 'python' in text.lower())
# print(python_jobs)

python_jobs_filtered = [job.get_text(strip=True) for job in python_jobs]

# python_job_cards = [
#     a_attribute.parent
# ]

if True:
    for job in python_jobs:
        title_element = job.get_text(strip=True)
        
        location_element = job.find_next("span", class_="listing-location")
        
        if location_element:
            location = location_element.get_text(strip=True)
        else:
            location = "Location not found"
        
        print(title_element)

        print(location)
