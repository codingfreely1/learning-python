import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
nytimes_web_page = requests.get(url)
soup = BeautifulSoup(nytimes_web_page.text, "lxml")
headers = soup.find_all("h2", "story-heading")
count = 1
for h in headers:
    if h.a is not None:
        article_header = h.a.text.strip()
    else:
        article_header = h.text.strip()
    print str(count) + ". " + article_header
    count += 1
    