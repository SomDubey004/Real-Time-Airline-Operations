from ingestion.api_client import APIClient

client = APIClient()

posts = client.get_posts()

if posts:

    print(f"\nTotal Records Received: {len(posts)}")

    print("\nFirst Record:\n")

    print(posts[0])

else:

    print("No data received from API.")