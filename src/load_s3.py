import boto3
from io import StringIO
from datetime import datetime
from config.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME, AWS_REGION

def upload_to_s3(df):
    """
    Uploads a Pandas DataFrame to AWS S3 as a CSV file.
    """
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        
    
        filename = f"raw_data/spotify_tracks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        print(f"☁️ Uploading {len(df)} rows to S3 Bucket: {AWS_BUCKET_NAME}...")
        
        s3.put_object(
            Bucket=AWS_BUCKET_NAME, 
            Key=filename, 
            Body=csv_buffer.getvalue()
        )
        
        print(f"✅ Success: Data saved to s3://{AWS_BUCKET_NAME}/{filename}")
        
    except Exception as e:
        print(f"❌ Error in upload_to_s3: {e}")

if __name__ == "__main__":
    
    print("Run run_pipeline.py instead.")
