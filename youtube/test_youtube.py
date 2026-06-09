import os

from googleapiclient.discovery import build

from config.env_loader import *

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)

request = youtube.search().list(
    q="AWS",
    part="snippet",
    maxResults=5,
    type="video"
)

response = request.execute()

print("\nYouTube API Working\n")

for item in response["items"]:

    print(
        item["snippet"]["title"]
    )