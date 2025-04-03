print("\033c")

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

URL = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
countries_data = soup.find_all(class_ = 'col-md-4 country')

for country in countries_data:

    country_name = country.find(class_ = 'country-name').get_text(strip = True)    
    country_capital = country.find(class_ = 'country-capital').get_text(strip = True)
    country_population = country.find(class_ = 'country-population').get_text(strip = True)
    country_area = country.find(class_ = 'country-area').get_text(strip = True)
    
    print(country_name)
    print(f"Capital: {country_capital}")
    print(f"Population: {country_population}")
    print(f"Area: {country_area}")
    print()
    
