#Automation script which accept directory name from user and create log file in that directory which contains info of all running process

import os
import psutil
import datetime
import time
from sys import *

def ProcessDisplay(log_dir='Ganesha'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime('%d_%b_%y-%H_%M_%S')
    seperator = '-'*80
    log_path = os.path.join(log_dir,"GaneshaLog_%s.log"%(timestamp))
    f = open(log_path,'w')
    f.write(seperator+'\n')
    f.write("Process Logger :"+time.ctime()+'\n')
    f.write(seperator+'\n')

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for ele in listprocess:
        f.write("%s\n"%ele)

def main():
    print("Process Monitor to create log of all running processes in given directory")
    print("Application name :"+argv[0])
    print(argv[1])
    if len(argv) != 2:
        print("Invalid Number of Aurguments")
        exit()

    else:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to create log of all running processes in given directory")
            exit()

        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument")
            print("Example : script.py Demo")
            exit()
        else:
            try:
                ProcessDisplay(argv[1])
            
            except ValueError:
                print("Error : Invalid datatype of input")

            except Exception as e:
                print("Error :", e)

if __name__=="__main__":
    main()