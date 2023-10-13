# Application to send mail to the mail ID provided in csv file
import requests
import csv
import os
import re
import smtplib
from sys import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def is_connected():
    request = requests.get("http://www.google.com", timeout = 1)
    if request.status_code == 200:
        return True
    else:
        return False

def MailSender(id):
    #configure_setup
    sender_email = "mail id"
    sender_passcode = "password"
    receiver_email = id

    #Mail
    
    Subject = "Trial Mail"
    Message = """Hello Sir/Ma'am,
    Have a great day !
    This is auto generated mail.
    
    Thank You,
    Team XYZ"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Subject
    msg.attach(MIMEText(Message,'plain'))

    try :
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_passcode)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Failed to sent mail :", e)


def File_Reader(filename):
    if not os.path.exists(filename):
        print("Given file does not exist")
    else:
        data = []
        f = open(filename,'r')
        csv_reader = csv.reader(f)

        for row in csv_reader:
            data.append(row)

        f.close()
        return data

def main():

    print("Application name :", argv[0])

    if len(argv) !=2:
        print("Invalid Number of arguments")
        exit()
    else:
        if argv[1]=='-h' or argv[1]=='-h':
            print("Application to send mails to all mail ID provided in csv file")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("Usage : Application_name filepath")
            exit()

        else:
            try:
                mail_id = File_Reader(argv[1])

                if is_connected():
                    
                    for i in mail_id:
                        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

                        if re.match(pattern,i[0]):
                            print(i[0])
                            MailSender(i[0])
                        else:
                            pass
                else:
                    print("No intenet connection")

            except Exception as e:
                print("Error :", e)

if __name__=="__main__":
    main()