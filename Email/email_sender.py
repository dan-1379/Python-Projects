import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # allows access to HTML file

html = Template(Path("index.html").read_text())

email = EmailMessage()
email["from"] = "" # ENTER THE EMAIL YOU WANT TO APPEAR AS THE SENDER
email["to"] = "" # ENTER THE EMAIL OF THE PERSON YOU WANT TO SEND THE EMAIL TO
email["subject"] = "" # ENTER THE EMAIL SUBJECT

email.set_content(html.substitute(name = "Bobby"), "html") # ENTER THE CONTENT OF THE MESSAGE TO BE SENT

with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("", "") # ENTER LOGIN DETAILS
    smtp.send_message(email)
    print("All good boss!")