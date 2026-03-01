import json

FILE_PATH = "calibration.json"

def save(data):
    print("Saving data:", data)
    try:
        with open(FILE_PATH, "w") as f:
            f.write(json.dumps(data))
        print("Save complete.")
    except OSError as e:
        print("Failed to save:", e)

def load():
    print("Loading data...")
    try:
        with open(FILE_PATH, "r") as f:
            return json.loads(f.read())
    except (OSError, ValueError):
        print("No configuration found.")
        return {}