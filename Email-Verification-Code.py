import os
from dotenv import load_dotenv
import smtplib
import random
from email.mime.text import MIMEText

load_dotenv() 

FROM = os.getenv("EMAIL_SENDER")
TO = os.getenv("EMAIL_RECEIVER")
keyy_password = os.getenv("EMAIL_PASSWORD")

msg = MIMEText(f'your Verification code : {code}')
msg['Subject'] = 'code Email'
msg['From'] = FROM
msg['To'] = TO

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(FROM, keyy_password)
        server.sendmail(FROM,TO,msg)
    print("send done")
except Exception as e:
    print("ERROR : ", e)


UserInputCode = input("write code : ")
if str(code) == UserInputCode.strip():
    print("TRUE")
else:
    print("This code is not correct")
