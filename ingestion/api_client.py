"""
API Client Module
-----------------
Handles communication with external APIs.
"""

import requests
from requests.exceptions import RequestException
from config.config import API_URL, API_TIMEOUT


class APIClient:

    def get_posts(self):

        print("Sending request to API...")

        try:

            response = requests.get(
                API_URL,
                timeout=API_TIMEOUT
            )
            
            response.raise_for_status()

            print("API request successful.")

            return response.json()

        except RequestException as e:

            print(f"API Error: {e}")

            return None