import csv
import json
from pathlib import Path
student = []

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "data.csv" , "r") as csv_file:
    read_data = csv.DictReader(csv_file)

    for row in read_data:
        row["name"] = row['name']
        row["age"] = int(row["age"])
        row["marks"] = int(row["marks"])
        student.append(row)
    
with open(BASE_DIR / "written.json" , "w") as f:
    json.dump(student,f,indent=4)
