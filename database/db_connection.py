"""
Database Connection Module

Purpose:
Provides a reusable connection to the MySQL database for the ETL pipeline.
"""

import psycopg

from config.config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
)


def get_connection():
    """
    Creates and returns a PostgreSQL database connection.
    """

    connection = psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    return connection