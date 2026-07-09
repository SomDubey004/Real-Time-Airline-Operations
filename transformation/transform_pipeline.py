"""
Transformation pipeline.

Coordinates all transformation steps.
"""

from transformation.flatten import flatten_all_flights


def transform(api_response):
    """
    Runs the complete transformation stage.
    """

    flattened_flights = flatten_all_flights(api_response)

    return flattened_flights
