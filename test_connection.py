from database.db_connection import get_connection

connection = get_connection()

if connection.is_connected():
    print("Database connection successful!")

connection.close()