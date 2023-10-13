import pywhatkit as kit
import os
import csv

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
    

def Messenger(number):

    message = "Hello from Python"
    kit.sendwhatmsg(number,message,22,41)
    print("Message sent...")

def main():

    Messenger("+91")

if __name__=="__main__":
    main()
