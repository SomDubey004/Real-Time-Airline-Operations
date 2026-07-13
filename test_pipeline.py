from ingestion.flight_pipeline import FlightETLPipeline

pipeline = FlightETLPipeline()

# step 1: extract data from API
data = pipeline.extract_data()

if data:

    # step 2: save raw data to file
    filename = pipeline.save_raw_data(data)

    print("Saved to:", filename)
    print("Flights:", len(data.get("data", [])))

    # step 3: transform data and load into database
    transformed = pipeline.transform_data(data)

    print(f"valid flights loaded: {len(transformed)}")