# Kafka Configuration

KAFKA_BROKER = "localhost:9092"

# Kafka Topics

NEWS_TOPIC = "news_data"
YOUTUBE_TOPIC = "youtube_stream"
TREND_TOPIC = "trend_data"

# Legacy topic (optional)
KAFKA_TOPIC = "tech_trends"

# AWS (future)

AWS_REGION = "ap-south-1"
S3_BUCKET = "ai-trend-lake"

# Data Sources

KEYWORDS = [
    "ChatGPT",
    "AWS",
    "Azure",
    "Databricks",
    "Kafka",
    "Snowflake",
    "LangChain"
]