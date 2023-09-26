#design automation script which accepts two directory names. copy all files from first directory into second. 
#second directory should be created at runtime

from sys import *
import os

def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)==2:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to copy files from given directory")
            exit()

        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument Second_Aurgument")
            print("Example : script.py Demo Temp")
            exit()
        else:
            print("Given aurgument is incorrect, try again with 'H' or 'U'")
            exit()

    if len(argv)==3:
        try:
            Current_directory = argv[1]
            new_directory = argv[2]

        except ValueError:
            print("Invalid input datatype")

        except Exception as E:
            print("Error :", E)

if __name__ =="__main__":
    main()