#Application to send mail to mail ID and corresponding msg in given csv file 
import csv
import os
import re
import requests
from sys import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def is_connected():
    request = requests.get("http://www.google.com")
    if request.status_code == 200:
        return True
    else:
        return False
    
def MailSender(receiver, message):
    #config_setup
    sender_id = input("Enter your mail id :")
    passcode = input("Enter your password :")
    receiver_id = receiver

    msg = MIMEMultipart()
    msg['From'] = sender_id
    msg['To'] = receiver_id
    msg['Subject'] = "Customized Mail"
    msg.attach(MIMEText(message,'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_id,passcode)
        server.sendmail(sender_id,receiver_id,msg.as_string())
        server.quit()
        print("Mail send successfully")

    except Exception as e:
        print("Unable to send mail :", e)




def FileReader(path):
    if not os.path.exists(path):
        print("Invalid file path")
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
            print("Application to send mails to mail ID and message provided in csv file")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("Usage : Application_name filepath")
            exit()

        else:
            try:
                result = FileReader(argv[1])

                if is_connected():
                    for i in result:
                        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                        if re.match(pattern, i[0]):
                            MailSender(i[0],i[1])

                else:
                    print("Interned is not connected")   

            except Exception as e:
                print("Error :", e)

if __name__=="__main__":
    main()