import csv
from sys import *
import os
import psutil
import datetime as ds

def Process_Log():
    listprocess = []
    try:
        for proc in psutil.process_iter():
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
    
    except (psutil.NoSuchProcess,psutil.AccessDenied, psutil.ZombieProcess):
        pass
    
    return listprocess

def Create_csv(process,dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    timestamp = ds.datetime.now().strftime('%d-%b-%y_%H-%M-%S')

    filename = 'process_%s.csv'%(timestamp)
    path = os.path.join(dirname,filename)

    with open(path,'w',newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        for row in process:
            csv_writer.writerow(row)

    csv_file.close()

    print("CSV log file created successfully")


def main():
    print("Automation Script Name : ", argv[0])

    if len(argv) !=2:
        print("Invalid Number of arguemtns")
        exit()

    if argv[1]=='-h' or argv[1]=='-H':
            print("This script use to create csv records of running processes")
            exit()

    elif argv[1]=='-u' or argv[1]=='-U':
        print("Usage : Script_Name First_Aurgument")
        print("Example : script.py Demo")
        exit()
    
    else:
        try:
            running_proc = Process_Log()

            for i in running_proc:
                print(i)

            Create_csv(running_proc,argv[1])
        except Exception as e:
            print("Error :", e)

if __name__=="__main__":
    main()