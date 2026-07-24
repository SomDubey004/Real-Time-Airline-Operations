"""
Main ETL Pipeline
-----------------
Coordinates the ETL workflow.
"""

import json
import os
import time
from datetime import datetime
from ingestion.api_client import APIClient
from transformation.transform_pipeline import FlightTransformer
from loading.flight_loader import FlightLoader
from utils.logger import get_logger


class FlightETLPipeline:

    def __init__(self):
        self.api_client = APIClient()
        self.transformer = FlightTransformer()
        self.loader = FlightLoader()
        self.logger = get_logger()

        self.logger.info("Flight ETL Pipeline initialized.")

    def run(self):
        """
        Runs the ETL pipeline.
        """
        start_time = time.time()

        status = "SUCCESS"

        data = []
        flights_received = 0
        transformed = []
        load_result = {
            "processed_flights": 0,
            "loaded_flights": 0
        }
        rows_loaded = 0


        try:

            data = self.extract_data()

            if data:

                flights_received = len(data.get("data", []))

                self.logger.info(f"Received {flights_received} flights from API.")

                self.save_raw_data(data)

                transformed = self.transform_data(data)

                load_result = self.load_data(transformed)

                rows_loaded = load_result["loaded_flights"]

        except Exception as e:

            status = "FAILED"
            self.logger.exception(f"ETL pipeline failed: {e}")

        finally:
            
            end_time = time.time()
            duration = end_time - start_time

            self.log_pipeline_summary(
                status=status,
                flights_received=flights_received,
                valid_flights=len(transformed),
                row_loaded=rows_loaded,
                duration=duration
            )

        return {
            "status": status,
            "flights_received": flights_received,
            "valid_flights": len(transformed),
            "rows_loaded": rows_loaded,
            "execution_time": duration
        }

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
        Transforms the raw API response into validated and standardized flight records.
        """

        self.logger.info("Starting transformation...")

        transformed = self.transformer.transform(api_response)

        self.logger.info(f"Transformation completed. {len(transformed)} valid flights.")

        return transformed 
    
    def load_data(self, flights):
        """
        Loads the transformed flights into the PostgreSQL database.
        """
       
        return self.loader.load_flights(flights)

    def log_pipeline_summary(self, status, flights_received, valid_flights, row_loaded, duration):
        """
        Logs a summary of the ETL pipeline execution.
        """

        self.logger.info("=" * 50)
        self.logger.info("Flight ETL Pipeline Summary")
        self.logger.info("=" * 50)

        self.logger.info(f"Pipeline Status: {status}")
        self.logger.info(f"Flights received: {flights_received}")
        self.logger.info(f"Valid flights : {valid_flights}")
        self.logger.info(f"Rows loaded into PostgreSQL: {row_loaded}")
        self.logger.info(f"Execution Time: {duration:.2f} seconds")

        self.logger.info("=" * 50)
    
