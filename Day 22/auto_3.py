# auto script which accepts directory name and two file extensions from user and rename all files with first file extension with second
#ex Demo.txt = Demo.doc
from sys import *
import os

def CheckFile(Dirname,ext1):
    print("Scanning through Directory........"+Dirname)

    flag = os.path.isabs(Dirname)
    if flag == False:
        Dirname = os.path.abspath(Dirname)

    Files = []
    exist = os.path.isdir(Dirname)

    if exist:
        for Dirname, foldername, filename in os.walk(Dirname):
            for fname in filename:
                f_ext = os.path.splitext(fname)[1]
                if ext1 == f_ext:
                    file_path = os.path.join(Dirname,fname)
                    Files.append(file_path)

                    
        if len(Files)>=1:
            return Files
        else:
            print("Files with given extension are not in current directory")
            exit()

    else:
        print("Invalid Path Given")

def RenameFile(f_list, ext2):
    for file in f_list:
        new_name = os.path.splitext(file)[0]+ext2
        try:
            os.rename(file,new_name)
            
        except OSError as e:
            print("Error : ", e)
            exit()
    print("File renamed")


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

        Directory = argv[1]
        current_ext = argv[2]
        new_ext = argv[3]

        try:
            arr = CheckFile(Directory, current_ext)
            RenameFile(arr,new_ext)


        except ValueError:
            print("Invalid input datatype")
        except Exception as E:
            print("Error :", E)
    else:
        print("Invalid Number of Aurguments")

if __name__ == "__main__":
    main()