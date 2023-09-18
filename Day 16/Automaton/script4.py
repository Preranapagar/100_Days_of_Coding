#Automation script that receives directory name and file name from user, check if that file is present and then removes it

from sys import *
import os
import time

def Delete_from_Directory(dirname,filename):
    print("We are going to scan directory :", dirname)

    flag = os.path.isabs(dirname)
    if flag == False:
        dirname = os.path.abspath(dirname)

    exist = os.path.isdir(dirname)

    if exist:
        for foldername, subfoldername, fname in os.walk(dirname):
            for file_name in fname:
                if file_name == filename:
                    print("File is present in current directory :", file_name)
                    os.remove(os.path.join(foldername,file_name))
                    print("File removed from directory")

    else:
        print("Invalid Path")


def main():

    print("--------------------------Automation Script--------------------------")
    print("Automation script name :", argv[0])

    if (argv[1]=="-h" or argv[1]=="-H"):
        print("This script is used to perform remove the given file from directory")
        exit()

    elif(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : Name_of_script First_aurgument Second_aurgument")
        print("Example Demo.py Python file.txt")
        exit()

    if len(argv) != 3:
        print("Invalid Number of aurguments")
        exit()
    else:
        starttime = time.time()

        Delete_from_Directory(argv[1],argv[2])

        endtime = time.time()
        print("The script took time to execute :", endtime-starttime)

if __name__=="__main__":
    main()