import os

# Kafka Configuration

KAFKA_BROKER = os.getenv(
    "KAFKA_BROKER",
    "localhost:9092"
)

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

TREND_CATEGORIES = {
    "AI": [
        "Artificial Intelligence",
        "OpenAI",
        "Claude",
        "Gemini",
        "LLM",
        "Agentic AI",
        "ChatGPT",
        "Mistral",
        "Anthropic",
        "NVIDIA"
    ],

    "Cloud": [
        "AWS",
        "Azure",
        "GCP",
        "Kubernetes",
        "Docker"
    ],

    "Data Engineering": [
        "Kafka",
        "Databricks",
        "Spark",
        "Snowflake",
        "Airflow",
        "MinIO",
        "MongoDB"
    ],

    "Cybersecurity": [
        "Cybersecurity",
        "Zero Trust",
        "Ransomware",
        "SIEM",
        "SOC"
    ],

    "Software Engineering": [
        "Python",
        "Java",
        "React",
        "Next.js",
        "Rust"
    ]
}

TECH_KEYWORDS = []

for category_keywords in TREND_CATEGORIES.values():
    TECH_KEYWORDS.extend(category_keywords)