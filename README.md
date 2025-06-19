# 📚 Project: Book Category Analyzer

## 🎯 Goal
Use web scraping to calculate the average rating and price of books from the target site: [Books to Scrape](https://books.toscrape.com)

### Steps
- Extract books from the **first page** of all categories and export the data to a CSV file.
- Calculate the **average price** and **average rating** for each category, then save that analysis to a new CSV file.

---

## 🛠️ Design

Implement the following objects or utility classes:
- `home_page`: Extracts book data and allows user change category.
- `book_data_cleaner`: Cleans book data list and calculates stats from it.
- `csv_parser`: Outputs python list as a csv file.

---

## 📤 Output

Each book will include the following fields:
- `Title`
- `Price`
- `Availability`
- `Rating`
- `Category`

---

## 🧹 Data Cleaning

Clean raw `Price` and `Rating` values so they can be used for numerical analysis.

- **Price**: Remove currency symbols and convert to float.
- **Rating**: Convert string values (e.g. "Three") to integers (e.g. 3).

---

## 📊 Data Analysis

For each category, calculate the following:
- `average_price`
- `std_price` (standard deviation of price)
- `average_rating`
- `std_rating` (standard deviation of rating)

---

## 🚧 Status

Data scraping and cleaning complete.  
Data analysis implemented and integrated.