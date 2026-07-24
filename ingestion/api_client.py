"""
API Client Module
-----------------
Handles communication with external APIs.
"""

import requests
from requests.exceptions import RequestException

from config.config import (API_KEY, API_URL, API_TIMEOUT, API_LIMIT)
from utils import logger


class APIClient:

    def fetch_flights(self):
        """
        Fetch live flight data from AviationStack.
        """

        params = {
            "access_key": API_KEY,
            "limit": API_LIMIT
        }

        try:

            response = requests.get(
                API_URL,
                params=params,
                timeout=API_TIMEOUT
            )

            response.raise_for_status()

            return response.json()

        except RequestException as e:

            logger.error(f"API Error: {e}")

            return None