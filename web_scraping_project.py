print("\033c")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
import requests

URL = "https://www.python.org/jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# print(page.text)

# results = soup.find(li = 'listing-company')
# print(results)