#create log file for duplicates from directory as well as delete duplicates
from sys import *
import os
import hashlib

def Hashfile(path,blocksize=1024):
    obj = open(path,'rb')
    hasher = hashlib.md5()
    buf = obj.read(blocksize)

    while len(buf)>1:
        hasher.update(buf)
        buf = obj.read(blocksize)

    obj.close()
    return hasher.hexdigest()

def CreateLog(d,dir):
    result = list(filter(lambda x : len(x)>1,d.values()))

    if len(result)>=1:
        folder_name = os.path.basename(dir)
        file_name = 'dups_log'+folder_name
        obj = open(file_name,'a')

        data =''
        for i in result:
            data+='Identical Files :\n'
            for j in i:
                data+=f'{j}\n'
            data+='\n'
        obj.write(data)
        obj.close()
        print("log of duplicate files is created")
    else:
        print("No duplicate files in current directory")
        exit()

def DeleteDuplicates(d1,d2):
    result = list(filter(lambda x : len(x)>1,d1.values()))
    for subresult in result:
        for i in range(1,len(subresult)):
            file = subresult[i]
            path = d2[file]
            try:
                os.remove(path)
            except OSError as e:
                print("An error occured while removing file :", e)
    print("Duplicates Deleted")

def CheckSum(dir):
    print("Scanning Directory :", dir)

    flag = os.path.isabs(dir)
    if flag == False:
        dir = os.path.abspath(dir)

    dups = {}
    file_paths = {}

    exist = os.path.isdir(dir)
    if exist:
        for Dirname, Foldername, Filename in os.walk(dir):
            for file in Filename:
                f_path = os.path.join(Dirname,file)
                file_paths[file]=f_path
                checksum = Hashfile(f_path)
                if checksum in dups:
                    dups[checksum].append(file)
                else:
                    dups[checksum]=[file]
        
        CreateLog(dups,dir)
        DeleteDuplicates(dups,file_paths)
        
    else:
        print("Invalid Directory Path")

def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)!=2:
        print("Invalid Number of Aurguments")
        exit()
    else:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to create log of duplicate files in given directory and delete them")
            exit()

        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument")
            print("Example : script.py Demo")
            exit()
        else:
            try:
                CheckSum(argv[1])


            except Exception as e:
                print("Error :", e)


if __name__=="__main__":
    main()


