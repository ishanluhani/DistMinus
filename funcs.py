from googleapiclient.discovery import build
import smtplib
from email.message import EmailMessage


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


def send_email(to, kid_name, category, video_link):
    EMAIL_ADDRESS = 'ishanluhani@gmail.com'
    EMAIL_PASSWORD = "Your API KEY"

    msg = EmailMessage()
    msg['Subject'] = 'DistMinus Found some unwanted activities'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to

    heading = '''
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style type="text/css">
            h1{font-size:56px}
            h2{font-size:28px;font-weight:900}
            p{font-weight:100}
            td{vertical-align:top}
            #email{margin:auto;width:600px;background-color:#fff}
            </style>
        </head>
        '''

    msg.set_content(heading + f'''
        <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
        <div id="email">
            <table role="presentation" width="100%">
                <tr>
                    <td bgcolor="purple" align="center" style="color: white;">
                        <h1>DistMinus</h1>
                    </td>
            </table>
            <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
                <tr>
                    <td>
                        <h2>{kid_name} is watching {category} Videos</h2>
                        <p>Video Link: {video_link}</p>
                    </td>
                </tr>
            </table>
        </div>
        </body>
        </html>''', subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=l5UhWVjKpCo&ab_channel=GauravThakur'
    print(f'Video Url = {video_url}')
    print(f'Category = {extract_category(video_url)}')

    send_email('neetuluhani@gmail.com', 'Rahul', 'Entertainment', 'https://www.youtube.com/watch?v=X7U2_tVejy0&ab_channel=GauravThakur')
    print('Mail sent')