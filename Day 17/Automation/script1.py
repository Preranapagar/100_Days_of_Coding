#Automation script to find a largest file in directory
from sys import *
import os
import time

def Largest_File(DirName):
    print("We are scanning the directory :", DirName)

    Maxsize = 0
    MaxsizeFile = ""

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if exist:
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                f_path = os.path.join(foldername, fname)
                if (Maxsize < os.path.getsize(f_path)):
                    Maxsize = os.path.getsize(f_path)
                    MaxsizeFile = fname
        print("Maximun size file in directory is :",MaxsizeFile,"with", Maxsize ,"bytes")

    else:
        print("Invalid path")

    

def main():
    print("---------------------------------------Automation Script---------------------------------------")
    print("Script Name :", argv[0])

    if len(argv) !=2:
        print("Invalid Number of arguments")
        exit()

    if (argv[1]=='-h' or argv[1]=='-H'):
        print("This automation script is use to find the largest file in directory")
        exit()

    elif (argv[1]=='-u' or argv[1]=='U'):
        print("Usage : Name_of_script First Argument")
        print("Example : Script.py Demo")
        exit()
    
    else:
        starttime = time.time()
        Largest_File(argv[1])
        endtime = time.time()

        print("Time took to run a script is :", endtime - starttime)

if __name__=="__main__":
    main()