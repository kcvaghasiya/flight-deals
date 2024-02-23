import smtplib

from twilio.rest import Client
import os
TWILIO_SID = os.environ.get("twilio_sid")
TWILIO_AUTH_TOKEN = os.environ.get("twilio_auth_token")
TWILIO_VIRTUAL_NUMBER = os.environ.get("twilio_virtual_num")
TWILIO_VERIFIED_NUMBER = os.environ.get("twilio_verified_num")
MY_EMAIL = os.environ.get("my_email")
PASSWORD = os.environ.get("email_password")

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"New Low Price Flight!\n\n{message}".encode('utf-8')
                                )