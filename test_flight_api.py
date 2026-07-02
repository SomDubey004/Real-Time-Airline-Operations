from ingestion.api_client import APIClient
from utils.file_handler import save_raw_json

client = APIClient()

data = client.fetch_flights()

if data:

    filepath = save_raw_json(data)

    print(f"Saved to: {filepath}")

else:

    print("No data received.")