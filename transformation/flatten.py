from transformation.validation import validate_flight
from transformation.standardizer import standardize_flight
from utils.logger import get_logger

logger = get_logger()

"""
Flatten neated AviationStack/OpenSky flight JSON
into a relational structure suitable for MySQL.
"""

def flatten_flight(flight):
    """
    Converts one nested flight record
    into one flat dictionary.
    """

    flattened = {}

    flattened["flight_date"] = flight.get("flight_date")

    flattened["flight_status"] = flight.get("flight_status")

    flattened["airline_name"] = flight.get("airline",{}).get("name")

    flattened["flight_iata"] = flight.get("flight",{}).get("iata")

    flattened["departure_airport"] = flight.get("departure",{}).get("airport")

    flattened["departure_iata"] = flight.get("departure",{}).get("iata")

    flattened["departure_delay"] = flight.get("departure",{}).get("delay")

    flattened["arrival_airport"] = flight.get("arrival",{}).get("airport")

    flattened["arrival_iata"] = flight.get("arrival",{}).get("iata")

    flattened["arrival_delay"] = flight.get("arrival",{}).get("delay")

    return flattened 

def flatten_all_flights(api_response):
    """
    Converts all flight records from the API response
    into a list of flattened dictionaries.
    """

    flattened_flights = []

    flights = api_response.get("data", [])

    for flight in flights:

        flat = flatten_flight(flight)

        is_valid, reason = validate_flight(flat)

        if is_valid:
            flat = standardize_flight(flat)
            flattened_flights.append(flat)
        else:
            logger.warning(
                f"Flight {flat.get('flight_iata', 'UNKNOWN')} rejected: {reason}"
                )

    return flattened_flights