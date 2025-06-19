import csv
from pathlib import Path

OUTPUT_DIR = "../output/"
RAW_DIR = "raw/"
CLEAN_DIR = "clean/"
SCRAPER_DIR = "scraper/"

def write_file(file_name, header_data, page_data, directory=OUTPUT_DIR):
    Path(directory).mkdir(parents=True, exist_ok=True)
    print(f"Writing {file_name} to {directory}")
    with open(directory + file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header_data)
        for row in page_data:
            writer.writerow(row)
        file.close()


def write_data(dataset_name, header_data, raw_data, clean_data, scraper_name=SCRAPER_DIR):
    if(scraper_name[-1] != "/" or scraper_name[-1] != "\\"):
        scraper_name += "/"

    if raw_data is not None:
        raw_file_name = clean_string(dataset_name) + "_raw.csv"
        write_file(raw_file_name, header_data, raw_data, OUTPUT_DIR+scraper_name+RAW_DIR)

    clean_file_name = clean_string(dataset_name) + "_clean.csv"
    write_file(clean_file_name, header_data, clean_data, OUTPUT_DIR+scraper_name+CLEAN_DIR)



def clean_string(value):
    return value.strip().replace(" ", "_").replace("\n", "_")

