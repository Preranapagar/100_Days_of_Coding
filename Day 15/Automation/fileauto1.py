from sys import *
import os

def DirectoyTravel(DirName):
    print("We are going to scan the Directory :", DirName)

    for foldername, subfoldername, filename in os.walk(DirName):
        for fname in filename:
            print(fname)

def main():
    print("_______________Automation Script_______________")
    print("Automation Script Name :", argv[0])

    if(len(argv) !=2):
        print("Invalid Number of Aurguments")
        exit()

    if (argv[1] == "-h" or argv[1]== "-H"): #flag for displaying help
        print("This automation script is used to perform file automation")
        exit()

    elif (argv[1] == "-u" or argv[1]=="-U"): #flag displaying the usage of script
        print("Usage : Name_of_script First_Argument")
        print("Example : Demo.py Marvellous")
        exit()
    
    else:
        DirectoyTravel(argv[1])
        #logic
        



if __name__=="__main__":
    main()