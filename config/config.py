"""
Application Configuration
-------------------------
Stores configuration variables used across the project.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# =========================
# PostgreSQL Configuration
# =========================

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "airline_operations"
DB_USER = "postgres"
DB_PASSWORD = "123456"

# ==========================
# AviationStack API
# ==========================

API_URL = "https://api.aviationstack.com/v1/flights"
API_TIMEOUT = 10

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")