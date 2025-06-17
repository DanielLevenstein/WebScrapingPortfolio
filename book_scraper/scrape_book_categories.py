
from book_scraper.utils import csv_parser
from book_scraper.pages import home_page

if __name__ == '__main__':
    home_page = home_page.HomePage(home_page.URL)
    category_data = home_page.scrape_category_data_raw()
    csv_parser.write_file("category_clean.csv", home_page.get_book_data_headers(), home_page.clean_category_data(category_data))


