from src.extract import extract_spotify_data
from src.load_s3 import upload_to_s3

if __name__ == "__main__":
    # Step 1: Extract
    data = extract_spotify_data()
    from src.extract import extract_spotify_data
from src.load_s3 import upload_to_s3

if __name__ == "__main__":
    print("🚀 Starting ETL Pipeline...")
    
    # Step 1: Extract
    data = extract_spotify_data()
    
    # Step 2: Load (Only if extraction worked)
    if data is not None and not data.empty:
        upload_to_s3(data)
        print("🎉 Pipeline Finished Successfully.")
    else:
        print("⚠️ Pipeline stopped: No data extracted.")
    # Step 2: Load (only if data exists)
    if data is not None:
        upload_to_s3(data)