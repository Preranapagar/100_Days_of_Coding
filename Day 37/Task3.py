#application to send scheduled mail to given id on a given date in csv file

import csv
import time
import os
from sys import *
import datetime
import requests
import smtplib
import schedule
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def is_connected():
    request = requests.get("http://www.google.com",timeout = 1)
    if request.status_code == 200:
        return True
    else:
        return False
    
def MailSender(id,mail):
    sender = "sender mail"
    password = "passcode"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = id
    msg['Subject'] = "Birthday Wish"
    msg.attach(MIMEText(mail,'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender,password)
        server.sendmail(sender,id,msg.as_string())
        server.quit()

        print("Msg sent successfully")
    
    except Exception as e:
        print("Error sending mail :", e)

def File_Reader(path):
    if not os.path.exists(path):
        print("File doesn't exist")
    else:
        data = []
        f = open(path,'r')
        csv_reader = csv.reader(f)

        for row in csv_reader:
            data.append(row)

        return data

def main():

    print("Application name :", argv[0])

    if len(argv) !=2:
        print("Invalid Number of arguments")
        exit()
    else:
        if argv[1]=='-h' or argv[1]=='-h':
            print("Application to send scheduled mails to all mail ID provided in csv file")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("Usage : Application_name filepath")
            exit()

        else:
            try:
                result = File_Reader(argv[1])

                for i in range(1,len(result)):
                    date_str = result[i][2]
                    format = "%d/%m/%Y"
                    date_obj = datetime.datetime.strptime(date_str,format)
                    date_f = date_obj.strftime("%H:%M")

                    if is_connected():
                        schedule.every().day.at(date_f).do(lambda : MailSender(result[i][0],result[i][1]))

                        while True:
                            schedule.run_pending()
                            time.sleep(1)
                    else:
                        print("No internet Connection")              

            except Exception as e:
                print("Error :", e)

if __name__=="__main__":
    main()