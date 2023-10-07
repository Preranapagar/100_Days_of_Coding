import os
import requests
import pandas as pd
from sys import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def is_connected():
    request = requests.get('http://www.google.com', timeout=1)
    if request.status_code == 200:
        return True
    else:
        return False
    
def MailSender(mail_id):
    #configuration setup
    sender_email = input("Enter Your Mail ID :")
    sender_passcode = input("Enter Your Password :")
    receiver_email = mail_id

    #Mail
    
    Subject = "Trail Mail"
    Message = """Hello Sir/Madam, 
    Have a great day !

    This is auto generated email.

    Thank you,
    Team"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Subject

    msg.attach(MIMEText(Message,'plain'))


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email,sender_passcode)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        server.quit()

        print("Email sent successfully !")
    
    except Exception as e:
        print("Failed to send mail :", e)

def main():

    df = pd.read_csv("mail.csv")

    for index in range(len(df)):
        row = df.loc[index]
        print(row)
    

if __name__=="__main__":
    main()