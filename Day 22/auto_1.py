#Automations script to display file from given directory using the given file extenstions

from sys import *
import os
import datetime as dt

def CreateLog(file):
    timestamp = dt.datetime.strftime(dt.datetime.now(),'%d-%b_%H-%M-%S')
    log_name = argv[1]+'_'+timestamp

    with open(log_name,'a') as obj:
        obj.write(file +'\n')

    obj.close()
    

def CheckDirectory(Dirname,extension):
    print("Scanning Directory..........", Dirname)

    flag = os.path.isabs(Dirname)
    if flag == False:
        Dirname = os.path.abspath(Dirname)

    Files = []
    exist = os.path.isdir(Dirname)

    if exist:
        for Dirname, foldername, filename in os.walk(Dirname):
            for fname in filename:
                f_extension = os.path.splitext(fname)[1]
                if f_extension == extension:
                    Files.append(fname)

        return Files
    else:
        print("Invalid Path")

def CheckFiles(data):
    if len(data)==0:
        print("File extensions you are looking for are not available in current directory")
    else:
        for i in data:
            CreateLog(i)
        print("Log created successfully..........")

def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)==2:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to get the names of specific extenstion file from given directory")
            exit()
        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument Second_Aurgument")
            print("Example : script.py Demo .pdf")
            exit()
        else:
            print("Given aurgument is incorrect, try again with 'H' or 'U'")
            exit()

    if len(argv)==3:
        Directory = argv[1]
        file_extention = argv[2]

        result =CheckDirectory(Directory,file_extention)
        CheckFiles(result)
        
    else:
        print("Invalid Number of Aurguments")
if __name__ == "__main__":
    main()
