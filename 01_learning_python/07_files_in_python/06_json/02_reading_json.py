import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "students.json" , "r") as f:
    data = json.load(f)
    print(data["Name"])
    print(data["Age"])
    print(data["Job"])