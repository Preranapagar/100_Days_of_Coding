import psutil
from sys import *
import os
import csv
import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def ProcessLog():
    listprocess = []
    try:
        for process in psutil.process_iter(attrs=['pid','name','username']):
            proc_info = process.info
            listprocess.append([
                proc_info['pid'],
                proc_info['name'],
                proc_info['username']
            ])
    except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
        pass

    return listprocess

def Create_CSV(process,dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    timestamp = datetime.now().strftime("%d-%b-%y_%H-%M-%S")
    filename = "%s_%s.csv"%(dirname,timestamp)
    filepath = os.path.join(dirname,filename)

    with open(filepath,'w',newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['PID','Name','Username'])
        writer.writerows(process)

    csv_file.close()

    print("CSV log generated.....")
    return filepath

def is_connected():
    request = requests.get('http://www.google.com', timeout=1)
    if request.status_code == 200:
        return True
    else:
        return False
    
def MailSender(mail_id):
    #configuration setup
    sender_email = input()
    sender_passcode = input()
    receiver_email = mail_id



    
def main():
    print("Name of Automation script :", argv[0])
    
    process = ProcessLog()
    Create_CSV(process,argv[1])

    if is_connected():
        MailSender(argv[2])
    else:
        print("Internet is not connected")


if __name__=="__main__":
    main()