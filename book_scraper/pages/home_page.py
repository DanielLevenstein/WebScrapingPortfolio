
import re
from book_scraper.pages.base_page import BasePage

IMAGE_CSS = "img"
PRICE_CSS = "p.price_color"
RATING_CSS = "p.star-rating"
AVAILABLE_CSS = "p.availability"
ARTICLE_CSS = "article"
SIDE_CATEGORIES_CSS = "div.side_categories a"
ratings_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

URL = "https://books.toscrape.com/catalogue/page-1.html"
BASE_URL = "https://books.toscrape.com/catalogue/"
class HomePage(BasePage):
    def __init__(self, url):
        super().__init__(url)

    def scrape_books_data_raw(self):
        books = self.__get_book_elements()
        book_data = []
        for book in books:
            book_data.append(self.__scrape_book_raw(book))
        return book_data

    def clean_book_data_clean(self, book_data):
        clean_data = []
        for book in book_data:
            clean_data.append(self.__clean_book_data(book))
        return clean_data

    def get_book_data_headers(self):
        return ["Title", "Price", "Availability", "Rating"]

    def __get_book_elements(self):
        return self.soup.find_all("article", class_="product_pod")

    def __scrape_book_raw(self, book_element):
        title = book_element.select_one(IMAGE_CSS).get("alt")
        price = book_element.select_one(PRICE_CSS).text.strip()
        available = book_element.select_one(AVAILABLE_CSS).text.strip()
        rating = book_element.select_one(RATING_CSS).get("class")[1].strip().lower()

        return [title, price, available, rating]

    def clean_books_data(self, books_data):
        for(book_data) in books_data:
            yield self.__clean_book_data(book_data)

    def __clean_book_data(self, book_data):
        clean_book_data = book_data.copy()
        clean_book_data[1] = re.sub(r"[^0-9.]", "", book_data[1])
        clean_book_data[3] = ratings_map.get(book_data[3])
        return clean_book_data

    def __get_category_elements(self):
        return self.soup.select(SIDE_CATEGORIES_CSS)

    def get_category_data_headers(self):
        return ["Category", "URL"]

    def scrape_category_data_raw(self):
        category_data = []
        for categories in self.__get_category_elements():
            category_data_row = [categories.text.strip(), BASE_URL+categories.get("href")]
            category_data.append(category_data_row)
        return category_data


    def clean_category_data(self, category_data):
        clean_category_data = []
        for category_row in category_data:
            category_data_row = [category_row[0].replace(" ","_"), BASE_URL+category_row[1]]
            clean_category_data.append(category_data_row)
        return clean_category_data


