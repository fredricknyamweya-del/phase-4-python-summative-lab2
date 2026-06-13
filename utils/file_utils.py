import os
import json

DATA_FILE = os.path.join("data", "db.json")

def load_data():
    """Load data from db.json. If file is missing, return empty structure."""
    if not os.path.exists(DATA_FILE):
        # Return a simple empty structure if db.json doesn't exist yet
        return {"users": [], "projects": [], "tasks": []}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading data: {e}")
        return {"users": [], "projects": [], "tasks": []}

def save_data(data):
    """Save data back into db.json safely."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")
