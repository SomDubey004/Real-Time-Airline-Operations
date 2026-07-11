"""
Transformation Pipeline
-----------------------
Coordinates all transformation steps.
"""

from transformation.flatten import flatten_all_flights


class FlightTransformer:
    """
    Runs the complete transformation pipeline.
    """

    def transform(self, api_response):
        """
        Transform API response into cleaned flight records.
        """

        print("Starting transformation...")

        flights = flatten_all_flights(api_response)

        print(f"Transformation completed. {len(flights)} valid flights.")

        return flights