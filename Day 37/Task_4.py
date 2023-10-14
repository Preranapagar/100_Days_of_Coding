import pywhatkit as kit
import os
import csv
from datetime import datetime , timedelta
from sys import *

def File_reader(path):
    if not os.path.exists(path):
        print("Invalid file path")
    else:
        data = []
        f = open(path,'r')
        csv_reader = csv.reader(f)
        for row in f:
            data.append(row)
        f.close()
        return data
    

def Messenger(number, h,m):

    message = "Hello, This message is sent using Python script. Good night"
    kit.sendwhatmsg(number,message,h,m)
    print("Message sent...")

def main():
    print("Application name :", argv[0])

    if len(argv) !=2:
        print("Invalid Number of arguments")
        exit()
    else:
        if argv[1]=='-h' or argv[1]=='-h':
            print("Application to send message to whatsapp number")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("Usage : Application_name filepath")
            exit()

        else:
            try:
                result = File_reader(argv[1])

                for i in range(1,len(result)):
                    time_for = datetime.now() + timedelta(minutes = 1)
                    hour = time_for.strftime('%H')
                    minute = time_for.strftime('%M')
                    Messenger(result[i],int(hour),int(minute))

            except Exception as e:
                print("Error :", e)

if __name__=="__main__":
    main()
