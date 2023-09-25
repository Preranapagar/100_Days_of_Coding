#Automation Script which accept directory name from user and display all names and checksum of files
from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize) 
    afile.close()
    return hasher.hexdigest()

def DisplayCheckSum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exist = os.path.isdir(path)

    if exist:
        for dirname, subdirname, filename in os.walk(path):
            print("Current Directory is :"+dirname)

            for file in filename:
                path = os.path.join(dirname,file)
                file_hash = hashfile(path)
                print(file ,":", file_hash)
                print(' ')
    else:
        print("Invalid Path")


def main():
    print("--------------------------Automation Script--------------------------")
    print("Script Name :", argv[0])

    if len(argv) !=2:
        print("Invalid number of arguments")
        exit()

    if argv[1]=='-h' or argv[1]=='-H':
        print("This script is use to get the name and checksum of files in given directory")
        exit()

    elif argv[1]=='-u' or argv[1]=='-U':
        print("Usage : Application_Name Absolute_Path_of_Directory")
        print("Example : Script.py Demo")
        exit()


    else:

        try:
            DisplayCheckSum(argv[1])

        except ValueError:
            print("Error : Invalid datatype of Input")

        except Exception as E:
            print("Error : Invalid Input ", E)

if __name__=="__main__":
    main()