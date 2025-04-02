print("\033c")

from bs4 import BeautifulSoup
import mechanicalsoup
from urllib.request import urlopen

# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")

# soup.find_all('img')

# image1, image2 = soup.find_all('img')

# image1.name

# image1["src"]
# image2["scr"]

# soup.title
# soup.title.string

# print(soup.find_all("img", scr = "/static/dionysus.jpg"))


# base_url = "http://olympus.realpython.org/profiles"
# page = urlopen(base_url)
# html_page = urlopen(base_url + "/profiles")
# html_text = page.read().decode('utf-8')
# soup = BeautifulSoup(html_text, "html.parser")

# for link in soup.find_all('a'):
#     link_url = base_url + link['href']
#     print(link_url)

browser = mechanicalsoup.Browser()

# username = zeus
# password = ThunderDude

url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]['value'] = 'zeus'
form.select("input")[1]['value'] = 'ThunderDude'

profiles_page = browser.submit(form, login_page.url)

print(profiles_page.url)

# print(page)
# prints the number of html lines

# print(type(page.soup))
# prints the type

# print(page.soup)
# prints out the page's html code
