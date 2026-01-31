import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
student = {
    "Name": "Arun",
    "Age": 22,
    "Job": "Developer for now (later will be system designer)"
}


with open(BASE_DIR / "written_json.json" ,"w") as f:
        data = json.dump(student, f, indent=4 )