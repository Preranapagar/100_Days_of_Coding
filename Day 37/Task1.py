# Application to send mail to the mail ID provided in csv file
import requests
import csv
import os
from sys import *

def is_connected():
    request = requests.get("http://www.google.com", timeout = 1)
    if request.status_code == 200:
        return True
    else:
        return False


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
                        print(i[0])
                else:
                    print("No intenet connection")

            except Exception as e:
                print("Error :", e)

if __name__=="__main__":
    main()