import requests
import smtplib
import datetime as ds
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def is_connected():
    try:
        request = requests.get('http://www.google.com',timeout=1)
        if request.status_code == 200:
            return True
        else:
            return False
    except:
        return False
    
def MailSender(filename,receiver_mail,time,scan_time,l):
    try:
        sender_email = 'your mail id'
        sender_password = 'passcode'
        receiver_email = receiver_mail

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,sender_password)

        Subject = "Deleted files Log Generated at : %s"%(time)

        msg = MIMEMultipart()

        body = """Hello %s,
        Please find attached documents which contains log of deleted files from directory.
        Log file created at : %s

        Starting time of Scanning : %s
        No of files scanned : %s
        No of duplicate files found : %s
        
        This is an auto generated mail
        Thanks & Regards,
        Your Name"""%(receiver_email,time,scan_time,l[0],l[1])

        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))
        attachment = open(filename,'rb')

        base = MIMEBase('application','octet-stream')
        base.set_payload((attachment).read())
        encoders.encode_base64(base)

        base.add_header('Content-Disposition','attachment; filename = %s'%filename)

        msg.attach(base)
        mail =msg.as_string()
        server.sendmail(sender_email,receiver_email,mail)

        server.quit()
        print("Log file successfully sent through mail")
    
    except Exception as E:
        print("Unable to send a mail :",E)
