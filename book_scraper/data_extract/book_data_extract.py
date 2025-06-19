import numpy
import re


ratings_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

def get_book_data_headers():
    return ["Title", "Price", "Availability", "Rating", "Category"]

def clean_books_data(books_data):
    for(book_data) in books_data:
        yield __clean_book_data(book_data)

def __clean_book_data(book_data):
    clean_book_data = book_data.copy()
    clean_book_data[1] = re.sub(r"[^0-9.]", "", book_data[1])
    clean_book_data[3] = ratings_map.get(book_data[3])
    return clean_book_data

def get_stat_headers():
    return ["Average Price", "STD Price", "Average Rating", "STD Rating", "Category"]
