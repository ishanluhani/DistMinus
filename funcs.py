from googleapiclient.discovery import build


def extract_category(video_url='https://www.youtube.com/watch?v=l5UhWVjKpCo&ab_channel=GauravThakur'):
    API_KEY = "YOUR API KEY (YOUTUBE API V3)"

    # Extract video ID from URL
    try:
        video_id = video_url.split("v=")[1].split("&")[0]
    except:
        video_id = video_url.split('/')[-1]

    # Build YouTube service
    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Get video details
    video_response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()

    # Extract video details
    category_id = video_response["items"][0]["snippet"]["categoryId"]

    category_response = youtube.videoCategories().list(
        part="snippet",
        id=category_id
    ).execute()
    category_name = category_response["items"][0]["snippet"]["title"]

    return category_name

if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=l5UhWVjKpCo&ab_channel=GauravThakur'
    print(f'Video Url = {video_url}')
    print(f'Category = {extract_category(video_url)}')