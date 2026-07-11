from database.db_connection import get_connection


def create_flights_table():
    """
    Creates the flights table if it doesn't already exist.
    """

    connection = get_connection()
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS flights (
        id SERIAL PRIMARY KEY,
        flight_date DATE,
        flight_status VARCHAR(50),
        airline_name VARCHAR(100),
        flight_iata VARCHAR(20),
        departure_airport VARCHAR(100),
        departure_iata VARCHAR(10),
        arrival_airport VARCHAR(100),
        arrival_iata VARCHAR(10),
        departure_delay INTEGER,
        arrival_delay INTEGER
    );
    """

    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()
    print("Flights table created successfully! (or already exists)")
    