# import Smart Mail Transfer Protocol
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


def send(toaddr):
    email = os.environ["EMAIL"]
    token = os.environ["TOKEN"]
    # creates SMTP server
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS for encryption
    s.starttls()

    # login using Google App Password
    s.login(email, token)

    # message to be sent
    message = "Hello!\nI just wanted to remind you that you promised to fight back against ageism!\nI wish you luck!\nAtharv"
    # send the mail
    s.sendmail(email, toaddr, message)
    # terminating the session
    s.quit()

