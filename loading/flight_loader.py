"""
Flight Loader

Responsible for loading transformed flight records
into PostgreSQL.
"""

from database.db_connection import get_connection
from utils.logger import get_logger

logger = get_logger()


class FlightLoader:

    def __init__(self):
        self.connection = get_connection()
        self.logger = get_logger()

    def load_flights(self, flights):
        """
        Loads a batch of flights into PostgreSQL.
        """

        cursor = self.connection.cursor()

        try:

            self.logger.info(
                f" Loading {len(flights)} flights into PostgreSQL..."
            )

            insert_query = """
            INSERT INTO flights (
                flight_date,
                flight_status,
                airline_name,
                flight_iata,
                departure_airport,
                departure_iata,
                arrival_airport,
                arrival_iata,
                departure_delay,
                arrival_delay
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s    
            )
            ON CONFLICT (flight_iata, flight_date)
            DO UPDATE SET
                flight_status = EXCLUDED.flight_status,
                airline_name = EXCLUDED.airline_name,
                departure_airport = EXCLUDED.departure_airport,
                departure_iata = EXCLUDED.departure_iata,
                arrival_airport = EXCLUDED.arrival_airport,
                arrival_iata = EXCLUDED.arrival_iata,
                departure_delay = EXCLUDED.departure_delay,
                arrival_delay = EXCLUDED.arrival_delay;
            """

            all_values = []

            for flight in flights:

                values = (
                    flight.get("flight_date"),
                    flight.get("flight_status"),
                    flight.get("airline_name"),
                    flight.get("flight_iata"),
                    flight.get("departure_airport"),
                    flight.get("departure_iata"),
                    flight.get("arrival_airport"),
                    flight.get("arrival_iata"),
                    flight.get("departure_delay"),
                    flight.get("arrival_delay")
                )

                all_values.append(values)

            if not all_values:
                self.logger.info("No valid flights to load.")
                return {
                    "processed_flights": 0,
                    "loaded_flights": 0
                }
            
            cursor.executemany(insert_query, all_values)

            self.connection.commit()

            self.logger.info(f"Successfully loaded {len(flights)} flights into PostgreSQL.")

            return {
                "processed_flights": len(flights),
                "loaded_flights": len(flights)
            }

        except Exception as e:

            self.connection.rollback()

            self.logger.error(f"Error loading flights: {e}")
            
            raise

        finally:
            
            cursor.close()