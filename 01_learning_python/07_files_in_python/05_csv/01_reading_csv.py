import csv
from pathlib import Path


BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "students.csv" , "r") as f:
    data = csv.reader(f)
    for row in data:
        print(row)
