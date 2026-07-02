"""
API Client Module
-----------------
Handles communication with external APIs.
"""

import requests
from requests.exceptions import RequestException

from config.config import API_KEY, API_URL, API_TIMEOUT


class APIClient:

    def fetch_flights(self):
        """
        Fetch live flight data from AviationStack.
        """

        params = {
            "access_key": API_KEY,
            "limit": 10
        }

        print("Requesting live flight data...")

        try:

            response = requests.get(
                API_URL,
                params=params,
                timeout=API_TIMEOUT
            )

            response.raise_for_status()

            print("Flight data received successfully.")

            return response.json()

        except RequestException as e:

            print(f"API Error: {e}")

            return None