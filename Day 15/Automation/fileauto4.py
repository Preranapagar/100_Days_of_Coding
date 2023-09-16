from sys import *
import os
import time

def DirectoyTravel(DirName):
    print("We are going to scan the Directory :", DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if exist :

        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current Directory Name :", foldername)

            for subname in subfoldername:
                print("Subfolder Name is :", subname)

            for fname in filename:
                print(fname)
                path =os.path.abspath(fname)
                print(path)
                print(os.path.getsize(path))

    else:
        print("Invalid Path")

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
        starttime = time.time()
        DirectoyTravel(argv[1])
        endtime = time.time()

        print("The Script took time to execture:", endtime-starttime)
        #logic


if __name__=="__main__":
    main()