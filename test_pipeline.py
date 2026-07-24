from ingestion.flight_pipeline import FlightETLPipeline

pipeline = FlightETLPipeline()

result = pipeline.run()

print("ETL Pipeline Result:")
print(result)