import boto3
from io import StringIO
from datetime import datetime
from config.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME, AWS_REGION

def upload_to_s3(df):
    """
    Uploads a Pandas DataFrame to AWS S3 as a CSV file.
    """
    try:
        # 1. Initialize S3 Client
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )
        
        # 2. Prepare the Buffer (In-memory CSV)
        # We use StringIO so we don't have to save a file to your hard drive first.
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        
        # 3. Create a unique filename
        # We add a timestamp so we don't overwrite yesterday's data.
        filename = f"raw_data/spotify_tracks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # 4. Upload
        print(f"☁️ Uploading {len(df)} rows to S3 Bucket: {AWS_BUCKET_NAME}...")
        
        s3.put_object(
            Bucket=AWS_BUCKET_NAME, 
            Key=filename, 
            Body=csv_buffer.getvalue()
        )
        
        print(f"✅ Success: Data saved to s3://{AWS_BUCKET_NAME}/{filename}")
        
    except Exception as e:
        print(f"❌ Error in upload_to_s3: {e}")

# Simple test block
if __name__ == "__main__":
    # If you run this file directly, it will fail because 'df' isn't defined.
    # We need to run this from run_pipeline.py
    print("Run run_pipeline.py instead.")