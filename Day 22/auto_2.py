# auto script which accepts directory name and two file extensions from user and rename all files with first file extension with second
#ex Demo.txt = Demo.doc
from sys import *
import os

def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)==2:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to rename the specific extenstion file from given directory")
            exit()
        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument Second_Aurgument Third_Aurgument")
            print("Example : script.py Demo .txt .doc")
            exit()
        else:
            print("Given aurgument is incorrect, try again with 'H' or 'U'")
            exit()

    if len(argv)==4:
        pass
    else:
        print("Invalid Number of Aurguments")

if __name__ == "__main__":
    main()