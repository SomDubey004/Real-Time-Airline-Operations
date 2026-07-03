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
    flattened["departure_delay"] = flight.get("departure",{}).get("delay")

    flattened["arrival_airport"] = flight.get("arrival",{}).get("airport")

    return flattened 

def flatten_all_flights(api_response):
    """
    Converts all flight records from the API response
    into a list of flattened dictionaries.
    """

    flattened_flights = []

    flights = api_response.get("data", [])

    for flight in flights:
        flat_record = flatten_flight(flight)
        flattened_flights.append(flat_record)

    return flattened_flights