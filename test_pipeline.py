from ingestion.flight_pipeline import FlightETLPipeline

pipeline = FlightETLPipeline()

data = pipeline.extract_data()

if data:
    filename = pipeline.save_raw_data(data)

    print("Saved to:", filename)
    print("Flights:", len(data.get("data", [])))