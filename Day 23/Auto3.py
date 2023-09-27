#Design script which accept directory name and find duplicate files form directory shown in logfile
from sys import *
import hashlib
import os

def Hashfile(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()
    return hasher.hexdigest()

def CheckDirectory(dir):
    print("Scanning directory :", dir)
    flag = os.path.isabs(dir)
    if flag == False:
        dir = os.path.abspath(dir)

    Dups = {}

    exist = os.path.isdir(dir)
    if exist:
        for Dirname, Foldername, Filename in os.walk(dir):
            for fname in Filename:
                f_path = os.path.join(Dirname,fname)
                checksum = Hashfile(f_path)
                if checksum in Dups:
                    Dups[checksum].append(fname)
                else:
                    Dups[checksum]=[fname]
        return Dups
    else:
        print("Invalid directory path")

def CreateLog(d):
    obj = open('Log.txt','a')
    result = list(filter(lambda x : len(x)>1, d.values()))
    if len(result)>=1:
        data =''
        for subresult in result:
            data+='duplicates files :\n'
            for sub in subresult:
                data+=f'{sub}\n'
            data+='\n'
        obj.write(data)
        print("Duplicates found in directory")
        obj.close()
    else:
        print("No duplicates")

def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)!=2:
        print("Invalid Number of Aurguments")
        exit()
    else:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to create log of duplicate files in given directory")
            exit()

        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument")
            print("Example : script.py Demo")
            exit()
        else:
            try:
                arr = CheckDirectory(argv[1])
                CreateLog(arr)

            except Exception as e:
                print("Error :", e)


if __name__=="__main__":
    main()