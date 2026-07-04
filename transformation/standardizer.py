"""
Standardization functions for flight data.
"""

def standardize_flight(flight):
    """
    Standardizes one flattened flight record.
    """

    if flight.get("airline_name"):
        flight["airline_name"] = flight["airline_name"].title()

    if flight.get("departure_airport"):
        flight["departure_airport"] = flight["departure_airport"].upper()

    if flight.get("arrival_airport"):
        flight["arrival_airport"] = flight["arrival_airport"].upper()

    return flight