from book_scraper.pages.home_page import HomePage
from book_scraper.data_extract.book_data_extract import get_book_data_headers
from book_scraper.utils import csv_parser
from book_scraper.pages import home_page

if __name__ == '__main__':
    home_page = HomePage(home_page.URL)
    category_data = home_page.scrape_category_data_raw()
    csv_parser.write_file("category_clean.csv", get_book_data_headers(), home_page.clean_category_data(category_data))


