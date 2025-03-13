import smtplib
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = os.environ['SMTP_USER']             #Set E-mail 
SMTP_PASSWORD = os.environ['SMTP_PASSWORD']     #Set Application Password

def lambda_handler(event, context):
    sns_message = json.loads(event["Records"][0]["body"])
    print(sns_message)

    if(sns_message["type"] == "error_message"):
        email = sns_message["email"]
        message = sns_message["message"]

        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg["To"] = email
        msg["Subject"] = "🚨 Application Exception Alert!"
        msg.attach(MIMEText(f"An error occurred:\n\n{message}", "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, email, msg.as_string())
        server.quit()

    return {"statusCode": 200, "body": "Email sent successfully!"}