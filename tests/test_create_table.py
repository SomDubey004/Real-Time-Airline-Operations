from loading.create_tables import create_flights_table

try:
    create_flights_table()
    print("table creation test completed successfully!")

except Exception as e:
    print(f"Table creation test failed: {e}")