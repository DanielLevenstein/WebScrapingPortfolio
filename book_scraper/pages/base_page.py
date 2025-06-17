import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/"
HOME_URL = "https://books.toscrape.com/catalogue/page-1.html"

class BasePage:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.content, "html.parser")
