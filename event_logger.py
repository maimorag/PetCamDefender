import json
from pathlib import Path

LOG_FILE = Path("events.json")

def log_event(event):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        json.dump(event, f)
        f.write("\n")