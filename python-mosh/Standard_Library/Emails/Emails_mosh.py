# how to get control email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())


message = MIMEMultipart()
message["from"] = "Jack Su"
message["to"] = "testuser@codwithmosh.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "Jack"})
message.attach(body, "html")
message.attach(MIMEImage(Path("mosh.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@codewithmosh.com", "todayskyblue1234")
    smtp.send_message(message)
    print("sent...")