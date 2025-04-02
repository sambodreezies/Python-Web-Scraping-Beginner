print("\033c")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import mechanicalsoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# print(page.text)

results = soup.find(id="ResultsContainer")
# print(results.prettify())

python_jobs = results.find_all(
    "h2", string = lambda text: "python" in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# print(len(python_jobs))
# print(python_jobs)

job_cards = results.find_all("div", class_ ="card-content")
# for job_card in python_job_cards:
#     # print(job_card, end="\n"*2)
    
#     title_element = job_card.find("h2", class_ = 'title')
#     company_element = job_card.find("h3", class_ = 'company')
#     location_element = job_card.find("p", class_ = 'location')
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print()


# python_jobs = results.find_all("h2", string = 'Python')
# print(python_jobs) 
# This will output an empty list becasue it looks for an exact match for 'Python'
# Any delineation will cause that value to not be returned

# for job_card in python_job_cards:
#     links = job_card.find_all("a")
#     for link in links:
#         print(link.text.strip())

# for job_card in python_job_cards:
#     links = job_card.find_all('a')
#     for link in links:
#         link_url = link["href"]
#         print(f"Apply here: {link_url}\n")

# for job_card in python_job_cards:
#     link_url = job_card.find_all("a")[1]["href"]
#     print(f"Apply here: {link_url}\n")


####### ALL TOGETHER NOW #######

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
