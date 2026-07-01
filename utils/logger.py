"""
Logger Module

Purpose:
Provides a reusable logger for the ETL pipeline.
"""

import logging
import os


def get_logger():
    """
    Creates and returns a logger that writes messages
    to both the terminal and a log file.
    """

    # Create the logs folder if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("airline_pipeline")

    # Prevent duplicate handlers if called multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Format for log messages
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File handler
    file_handler = logging.FileHandler("logs/pipeline.log")
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Attach handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger