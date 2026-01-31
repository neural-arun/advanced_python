import json
import csv
from pathlib import Path

books = []

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "book_data.csv" , "r") as f:
    data = csv.DictReader(f)

    for row in data:
        row["title"] = row["title"]
        row["price"] = int(row["price"])
        books.append(row)

with open( BASE_DIR / "written_books_date.json" , "w") as json_data:
    json.dump(books,json_data, indent=4)