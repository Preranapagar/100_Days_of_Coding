import psutil
from sys import *
import os
import time
import csv
import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


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
    
def MailSender(path,mail_id):
    #configuration setup
    sender_email = input("Enter Your Mail ID :")
    sender_passcode = input("Enter Your Password :")
    receiver_email = mail_id

    #Mail
    
    Subject = "Log of Running Processes created at : %s"%(time.ctime())
    Message = """Hello Sir/Madam, 
    This email contains log of all the running processes on your system.
    This is auto generated email.

    Thank you,
    Team"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Subject

    msg.attach(MIMEText(Message,'plain'))

    attachment = open(path,'rb')
    base = MIMEApplication(attachment.read(), Name = path)
    base['Content-Disposition'] = "attachemnt; filename = %s"%path
    
    msg.attach(base)

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
    print("Name of Automation script :", argv[0])
    
    process = ProcessLog()
    log_path = Create_CSV(process,argv[1])

    if is_connected():
        MailSender(log_path,argv[2])
    else:
        print("Internet is not connected")


if __name__=="__main__":
    main()