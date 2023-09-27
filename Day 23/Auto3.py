#Design script which accept directory name and find duplicate files form directory shown in logfile
from sys import *
import hashlib
import os

def CheckDirectory():
    pass

def CreateLog():
    pass

def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)!=2:
        print("Invalid Number of Aurguments")
        exit()
    else:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to duplicate files in given directory")
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


if __name__=="__main__":
    main()