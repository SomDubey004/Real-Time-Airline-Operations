"""
File handling utilities.
"""

import json
from datetime import datetime
from pathlib import Path


def save_raw_json(data, folder="data/raw"):
    """
    Save API response as a timestamped JSON file.
    """

    Path(folder).mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"flights_{timestamp}.json"

    filepath = Path(folder) / filename

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return filepath