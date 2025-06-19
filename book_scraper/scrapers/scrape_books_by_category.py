from book_scraper.pages.category_page import CategoryPage
from book_scraper.data_extract.book_data_extract import get_book_data_headers, clean_books_data, get_stat_data, get_stat_headers
from book_scraper.utils import csv_parser
from book_scraper.pages import home_page

if __name__ == '__main__':
    STARTING_INDEX = 1
    NAME_INDEX = 0
    HREF_INDEX = 1
    home_page = home_page.HomePage(home_page.URL)
    category_data = home_page.scrape_category_data_raw()
    all_data_raw = []

    index = 0
    for category in category_data:
        if index >= STARTING_INDEX:
            category_page = CategoryPage(category[HREF_INDEX])
            books_data = category_page.scrape_books_data_raw()
            clean_data = clean_books_data(books_data)
            all_data_raw.extend(books_data)
            file_name = category[NAME_INDEX]
            print(f"Writing {category[NAME_INDEX]} data")
            csv_parser.write_data(file_name, get_book_data_headers(), books_data, clean_data, "books_by_category")

        index += 1
    all_data_scraper_name = "all_books"
    csv_parser.write_data(all_data_scraper_name, get_book_data_headers(), all_data_raw, None, all_data_scraper_name)

    stats_data = get_stat_data(all_data_raw)
    csv_parser.write_data("category_stats", get_stat_headers(), None, stats_data, all_data_scraper_name)
