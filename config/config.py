"""
Application Configuration
-------------------------
Stores configuration variables used across the project.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ==========================
# Database Configuration
# ==========================

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "YOUR_MYSQL_PASSWORD"
DB_NAME = "flight_db"

# ==========================
# AviationStack API
# ==========================

API_URL = "https://api.aviationstack.com/v1/flights"
API_TIMEOUT = 10

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")