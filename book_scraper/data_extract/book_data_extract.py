from collections import defaultdict
from pdb import TESTCMD
from typing import List

import re

import numpy as np

ratings_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}

PRICE_INDEX = 1
RATING_INDEX = 3
CATEGORY_INDEX = 4

def get_book_data_headers():
    return ["Title", "Price", "Availability", "Rating", "Category"]

def clean_books_data(books_data):
    return[__clean_book_data(book) for book in books_data]

def __clean_book_data(book_data):
    clean_book_data = book_data.copy()
    clean_book_data[1] = float(re.sub(r"[^\d.]", "", book_data[1]))
    clean_book_data[3] = ratings_map.get(book_data[3])
    return clean_book_data

def get_stat_headers():
    return ["Average Price", "STD Price", "Average Rating", "STD Rating", "Category"]


def get_stat_data(raw_books_data):
    # casting input data to list to force program to calculate values
    list_data = clean_books_data(raw_books_data)
    category_data = defaultdict(lambda: {"prices": [], "ratings": []})

    for book in list_data:
        price = book[PRICE_INDEX]
        rating = book[RATING_INDEX]
        category = book[CATEGORY_INDEX]

        category_data[category]["prices"].append(price)
        category_data[category]["ratings"].append(rating)

    stat_data = []

    for category, values in category_data.items():
        prices = np.array(values["prices"])
        ratings = np.array(values["ratings"])

        avg_price = round(np.mean(prices), 2)
        std_price = round(np.std(prices, ddof=1), 2) if len(prices) > 1 else 0.0
        avg_rating = round(np.mean(ratings), 2)
        std_rating = round(np.std(ratings, ddof=1), 2) if len(ratings) > 1 else 0.0

        stat_data.append([
            avg_price,
            std_price,
            avg_rating,
            std_rating,
            category
        ])

    return stat_data


if __name__ == '__main__':
    test_data = [\
        ["Book Title 1 ",1.00, "In stock", 5, "Category"],
        ["Book Title 2", 2.00, "In stock", 4, "Category"],
        ["Book Title 3", 3.00, "In stock", 5, "Category"],
        ["Book Title 4", 4.00, "In stock", 4, "Category"],
        ["Book Title 5", 5.00, "In stock", 5, "Category"],
        ]
    get_stat_data_values = get_stat_data(test_data)
    print(get_stat_headers())
    print(get_stat_data_values)