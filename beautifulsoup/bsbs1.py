import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
for tag in soup.find_all(True):
    print(tag.name)
