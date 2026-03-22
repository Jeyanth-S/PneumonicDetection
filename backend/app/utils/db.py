import json
import os

class JSONDatabase:
    def __init__(self, db_file="db.json"):
        self.db_file = db_file

    def load(self):
        if not os.path.exists(self.db_file):
            return {}
        with open(self.db_file, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.db_file, "w") as f:
            json.dump(data, f, indent=2)