#Automation script that receives directory name and file name from user, check if that file is present and then removes it

from sys import *
import os
import time

def main():

    print("--------------------------Automation Script--------------------------")
    print("Automation script name :", argv[0])

    if (argv[1]=="-h" or argv[1]=="-H"):
        print("This script is used to perform remove the given file from directory")
        exit()

    elif(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : Name_of_script First_aurgument Second_aurgument")
        

if __name__=="__main__":
    main()