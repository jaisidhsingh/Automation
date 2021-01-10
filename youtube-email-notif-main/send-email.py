from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
import requests
import json


data = {}
with open("user.json") as f:
    data = json.load(f)

thumbnail_url = data["image_url"]
video_link = data["videos_url"]
video_title = data["title"]

#CREATE AN EMPTY JPG FILE AS "sample.jpg" TO OVERWRITE WITH THUMBNAIL CONTENT :
response = requests.get(thumbnail_url)
file = open("sample.jpg", "wb")
file.write(response.content)
file.close

message = MIMEMultipart()
message["from"] = "My Computer"
message["to"] = email
message.attach(MIMEText(f"New YouTube Video ! {video_title} Click here to watch : {video_link}"))
message.attach(MIMEImage(Path("sample.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, pw)
    smtp.send_message(message)
    print("Sent !")



