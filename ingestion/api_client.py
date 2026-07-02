"""
API Client Module
-----------------
Handles communication with external APIs.
"""

import requests
from requests.exceptions import RequestException


class APIClient:

    def get_posts(self):

        print("Sending request to API...")

        try:

            response = requests.get(
                "https://jsonplaceholder.typicode.com/posts",
                timeout=10
            )

            response.raise_for_status()

            print("API request successful.")

            return response.json()

        except RequestException as e:

            print(f"API Error: {e}")

            return None