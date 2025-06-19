from book_scraper.pages.home_page import HomePage
from book_scraper.data_extract.book_data_extract import get_book_data_headers
from book_scraper.utils import csv_parser
from book_scraper.pages import home_page


if __name__ == '__main__':
    home_page = HomePage(home_page.URL)
    csv_parser.write_file("home_clean.csv", get_book_data_headers(), home_page.scrape_books_data_raw())



    stats_data = get_stat_data(all_data_clean)
    csv_parser.write_data("category_stats", get_stat_headers(), None, stats_data, all_data_scraper_name)