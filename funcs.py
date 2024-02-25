from credentials import *
from googleapiclient.discovery import build
from email.message import EmailMessage
from twilio.rest import Client
import smtplib


def extract_category(video_url='https://www.youtube.com/watch?v=l5UhWVjKpCo&ab_channel=GauravThakur'):
    # Extract video ID from URL
    try:
        video_id = video_url.split("v=")[1].split("&")[0]
    except:
        video_id = video_url.split('/')[-1]

    # Build YouTube service
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

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


def send_sms(to, child_name, category, video_link):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        from_='+14152758275',
        to=f'+91{to}',
        body=f'''
        DistMinus Found some unwanted activities

        Your child {child_name} is found watching {category} videos when he is not supposed to.

        Video link: {video_link}'''
    )


if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=l5UhWVjKpCo&ab_channel=GauravThakur'
    category = extract_category(video_url)
    print(f'Video Url = {video_url}')
    print(f'Category = {category}')

    send_email(RECEIVERS_EMAIL_ID, 'Rahul', category, video_url)
    print('Mail sent')

    send_sms(RECEIVERS_PHONE_NO, 'Rahul', category, category)
    print('SMS Sent Successfully')
