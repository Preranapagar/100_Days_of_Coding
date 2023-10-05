import psutil
from sys import *
import os
import csv
from datetime import datetime

def ProcessLog():
    listprocess = []
    try:
        for process in psutil.process_iter(attrs=['pid','name','username']):
            proc_info = process.info()
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
    filename = "Dirname_%s.csv"%timestamp
    filepath = os.path.join(dirname,filename)

    with open(filepath,'w',newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['PID','Name','Username'])
        writer.writerows(process)

    csv_file.close()

    print("CSV log generated.....")

    
def main():
    print("Name of Automation script :", argv[0])
    
    process = ProcessLog()
    Create_CSV(process,argv[1])

if __name__=="__main__":
    main()