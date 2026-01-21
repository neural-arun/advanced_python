import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent



data = [
    ["name", "age", "marks"],
    ["Arun", 18, 92],
    ["Rahul", 19, 85]
]


with open(BASE_DIR / "written_csv" , "w" , newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)