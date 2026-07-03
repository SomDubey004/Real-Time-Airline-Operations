"""
Explore a raw JSON file.
"""

import json
from pathlib import Path


# Locate the raw data folder
raw_folder = Path("data/raw")

# Get all JSON files
json_files = sorted(raw_folder.glob("*.json"))

# Check whether any files exist
if not json_files:
    print("No JSON files found.")
    exit()

# Select the newest file
latest_file = json_files[-1]

print(f"Reading file: {latest_file.name}")

# Open the JSON file
with open(latest_file, "r", encoding="utf-8") as file:
    data = json.load(file)

print("\nJSON loaded successfully!")

# Exploring JSON file
print("\n========== JSON EXPLORATION ==========")

# Print the type of the JSON object
print(f"\nTop-level Python object: {type(data)}")

# Print the top-level keys
print("\nTop-level keys:")

for key in data.keys():
    print(f"- {key}")

# Count the number of flight records
flight_records = data.get("data", [])

print(f"\nNumber of flight records: {len(flight_records)}")

# Inspecting one flight record
if flight_records:

    first_flight = flight_records[0]

    print("\nKeys inside the first flight record:\n")

    for key in first_flight.keys():
        print(f"- {key}")