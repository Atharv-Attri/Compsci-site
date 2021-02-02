# import Smart Mail Transfer Protocol
import smtplib
import os


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
    message = """<text you want>"""
    i = 0
    num = 50  # the number of emails you want to send
    while i < num:
        # send the mail
        s.sendmail(email, toaddr, message)
        print("sent email")
        # terminating the session
    s.quit()
