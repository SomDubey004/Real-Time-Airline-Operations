"""
Validation functions for flattened flight data.
"""

def validate_flight(flight):
    """
    Validates one flattened flight record.

    Returns:
        tuple: (is_valid, reason)
    """

    if not flight.get("flight_date"):
        return False, "Missing flight_date"
    
    if not flight.get("airline_name"):
        return False, "Missing airline_name"
    
    if not flight.get("departure_airport"):
        return False, "Missing departure_airport"
    
    if not flight.get("arrival_airport"):
        return False, "Missing arrival_airport"
    
    if not flight.get("flight_iata"):
        return False, "Missing flight number"

    return True, "Valid"