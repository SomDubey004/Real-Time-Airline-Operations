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
            );
            """

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

                cursor.execute(insert_query, values)

            self.connection.commit()

        except Exception as e:

            self.connection.rollback()

            self.logger.error(f"Error loading flights: {e}")
            
            raise

        finally:
            
            cursor.close()