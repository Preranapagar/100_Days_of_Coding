#design automation script which accepts two directory name and one file extension
#copy all files with that extension to second directory which should be created at runtime

import os
from sys import *
import shutil 

def CheckDir(dir,ext):
    print("Scanning Directory :" ,dir)
    flag = os.path.isabs(dir)
    if flag == False:
        dir = os.path.abspath(dir)

    Files = []
    exist = os.path.isdir(dir)
    if exist:
        parent_path = os.path.dirname(dir)
        for dirname , foldername, filename in os.walk(dir):
            for fname in filename:
                f_ext = os.path.splitext(fname)[1]
                if f_ext == ext:
                    file_path = os.path.join(dirname,fname)
                    Files.append(file_path)
        if len(Files)>=1:
            return Files , parent_path
        else:
            print("File with given extension are not in current directory")
            exit()
    else:
        print("Invalid Path")

def CreateDirectory(path, dir):
    new_path = os.path.join(path,dir)
    exist = os.path.isdir(new_path)

    if exist:
        print("Directory with given name alredy exist, please provide diffrent name")
        exit()
    else:
        try:
            os.mkdir(new_path)
            print("New Directory Created")
            return new_path
        except OSError as e:
            print("Error :", e)

def CopyingFiles(Files,destination):

    for file in Files:
        try : 
            shutil.copy(file,destination)
            print("File Copied")
        except FileNotFoundError:
            print("File Not Found")
        except Exception as e:
            print("Error :", e)
        

def main():
    print("-"*55,"Automation Script","-"*55)
    print("Automation Script Name :", argv[0])

    if len(argv)==2:
        if argv[1]=='h' or argv[1]=='H':
            print("This script use to copy files with specific extension from given directory to another")
            exit()

        elif argv[1]=='u' or argv[1]=='U':
            print("Usage : Script_Name First_Aurgument Second_Aurgument Third_Aurgument")
            print("Example : script.py Demo Temp .txt")
            exit()
        else:
            print("Given aurgument is incorrect, try again with 'H' or 'U'")
            exit()

    if len(argv)==4:
        try:
            source_dir = argv[1]
            destination_dir = argv[2]
            file_ext = argv[3]

            result = CheckDir(source_dir,file_ext)

            new_result = CreateDirectory(result[1],destination_dir)

            CopyingFiles(result[0],new_result[0])

        except ValueError:
            print("Invalid input datatype")

        except Exception as E:
            print("Error :", E)
    else:
        print("Invalid Number of Aurguments")

if __name__=="__main__":
    main()