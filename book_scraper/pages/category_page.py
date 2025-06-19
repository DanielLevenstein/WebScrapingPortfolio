
from book_scraper.pages.home_page import HomePage


BASE_URL = "https://books.toscrape.com/catalogue/"
class CategoryPage(HomePage):
    def __init__(self, category_url):
        super().__init__(category_url)
