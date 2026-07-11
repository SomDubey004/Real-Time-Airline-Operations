"""
Main ETL Pipeline
-----------------
Coordinates the ETL workflow.
"""

import json
import os
from datetime import datetime
from venv import logger
from ingestion.api_client import APIClient
from transformation.transform_pipeline import FlightTransformer
from utils.logger import get_logger


class FlightETLPipeline:

    def __init__(self):
        self.api_client = APIClient()
        self.transformer = FlightTransformer()
        self.logger = get_logger()

        self.logger.info("Flight ETL Pipeline initialized.")

    def extract_data(self):
        """
        Extracts live flight data from the API.
        """

        self.logger.info("Starting extraction...")

        api_response = self.api_client.fetch_flights()

        if api_response is None:
            self.logger.error("Extraction failed.")
            return None

        self.logger.info("Extraction completed successfully.")

        return api_response
    
    def save_raw_data(self, api_response):
        """
        Saves the raw API response to the data/raw folder.
        """

        os.makedirs("data/raw", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/raw/flights_{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(api_response, f, indent=4)

        self.logger.info(f"Raw data saved to {filename}")

        return filename
    
    def transform_data(self, api_response):
        """
        Transforms the raw API response into cleaned flight records.
        """

        logger.info("Starting transformation...")

        transformed = self.transformer.transform(api_response)

        logger.info(f"Transformation completed. {len(transformed)} valid flights.")

        return transformed 
    
    