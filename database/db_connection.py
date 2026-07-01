"""
Database Connection Module

Purpose:
Provides a reusable connection to the MySQL database for the ETL pipeline.
"""

import mysql.connector

from config.config import (
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
)


def get_connection():

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    return connection