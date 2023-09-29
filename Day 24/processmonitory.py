#automation script which accepts time interval from user and create log file that Marvellous directory which contains
#information of all running processes. after creating that log file send that log file through mail

import os
import time
import psutil
import urllib2
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout = 1)
        return True
    except urllib2.URLError as err:
        return False
    
def MailSender(filename,time):
    try:
        fromaddr = "pagar.prerana@gmail.com"
        toaddr = "pagar.prerana333@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to Prerana Infosystems.
        Please find attached document which contains Log of Running process.
        Log file is created at : %s
        
        This is auto generated mail
        Thank & Regards,
        Prerana Pagar""" %(toaddr,time)

        Subject = "Prerana Infosystem Process Log generated at : %s"%(time)

        msg['Subject'] = Subject
        msg.attach(MIMEText(body,'plain'))
        attachment = open(filename,'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_playload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', 'attachment; filename = %s'%filename)

        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(fromaddr,"---------")

        text = msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        s.quit()

        print("Log file successfully sent through Mail")

    except Exception as e:
        print("Unable to send mail :", e)

