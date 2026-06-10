import boto3
from pathlib import Path

MINIO_ENDPOINT = "http://minio:9000"
ACCESS_KEY = "admin"
SECRET_KEY = "password123"
BUCKET_NAME = "ai-trend-lake"

s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

analytics_path = Path("data-lake/analytics")

files_to_upload = [
    "sentiment_summary.json",
    "trending_keywords.json",
    "unified_trend_scores.json",
    "ai_summary.json"
]

for filename in files_to_upload:

    file_path = analytics_path / filename

    if file_path.exists():

        s3.upload_file(
            str(file_path),
            BUCKET_NAME,
            f"analytics/{filename}"
        )

        print(f"✅ Uploaded {filename}")

print("\n🚀 Analytics upload completed.")