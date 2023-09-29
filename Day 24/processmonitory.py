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

def ProcessLog(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = '-'*80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(seperator+'\n')
    f.write("Prerana Infosystem Process Logger :"+time.ctime()+'\n')
    f.write(seperator+'\n')
    f.write('\n')

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for ele in listprocess:
        f.write("%s\n"%ele)

    print("Log file successfully generated at location %s"%log_path())

    connected = is_connected()

    if connected:
        starttime = time.time()
        MailSender(log_path,time.ctime())
        endtime = time.time()

        print('Took %s second to send mail'%(endtime-starttime))
    else:
        print("There is no internet connection")

def main():
    print("Prerana Infosystem")
    print("Application name :", argv[0])

    if len(argv) !=2:
        print("Invalid Number of Aurguments")
        exit()

    if argv[1]=='-h' or argv[1]=='-H':
            print("This script use to create log records of running processes")
            exit()

    elif argv[1]=='-u' or argv[1]=='-U':
        print("Usage : Script_Name First_Aurgument")
        print("Example : script.py Demo")
        exit()
    
    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Invalid data type of input")

    except Exception as e:
        print("Error :"+e)

if __name__ == "__main__":
    main()


