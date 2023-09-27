#Automation script which accepts directory name an display checksum of all files in log

from sys import *
import os
import hashlib
import datetime as dt

def CheckSum(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buffer = fd.read(blocksize)

    while len(buffer)>0:
        hasher.update(buffer)
        buffer = fd.read(blocksize)

    fd.close()
    return hasher.hexdigest()


def CheckDirectory(Dirname):
    print("Scanning through directory :", Dirname)

    flag = os.path.isabs(Dirname)
    if flag == False:
        Dirname = os.path.abspath(Dirname)

    Hash_dict = {}
    exist = os.path.isdir(Dirname)

    if exist:
        for dirname , foldername, filename in os.walk(Dirname):
            for fname in filename:
                f_path = os.path.join(dirname,fname)
                file_Checksum = CheckSum(f_path)
                Hash_dict[fname] = file_Checksum
        print("Checksum calculated")
        return Hash_dict
        
    else:
        print("Invalid Directory Path")

def CreateLog(logs, name):
    timestamp = dt.datetime.now().strftime('%d-%b-%H-%M-%S')
    log_name = name+timestamp
    with open(log_name,'a') as log:
        for key , value in logs.items():
            data = f'{key} :{value}\n'
            log.write(data)
    log.close()
    print("Log created")
    

 
def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)!=2:
        print("Invalid Number of Aurguments")
        exit()
    else:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to calculate checksum of files in given directory")
            exit()

        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument")
            print("Example : script.py Demo")
            exit()
        else:
            try:
                arr = CheckDirectory(argv[1])
                CreateLog(arr,argv[0])

            except Exception as e:
                print("Error :", e)

if __name__ == "__main__":
    main()