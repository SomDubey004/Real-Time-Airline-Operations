"""
Main ETL Pipeline
-----------------
Coordinates the ETL workflow.
"""

import json


class FlightETLPipeline:

    def __init__(self):
        print("Flight ETL Pipeline Created")

    def extract_data(self):

        print("Reading flight JSON file...")

        with open("data/raw/flights.json", "r") as file:
            flights = json.load(file)

        print("Flight data extracted successfully.")

        return flights