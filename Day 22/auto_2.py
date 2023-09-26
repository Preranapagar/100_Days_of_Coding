# auto script which accepts directory name and two file extensions from user and rename all files with first file extension with second
#ex Demo.txt = Demo.doc
from sys import *
import os

def RenameFile(Dirname,ext1,ext2):
    print("Scanning through Directory........"+Dirname)

    flag = os.path.isabs(Dirname)
    if flag == False:
        Dirname = os.path.abspath(Dirname)

    exist = os.path.isdir(Dirname)

    if exist:
        for Dirname, foldername, filename in os.walk(Dirname):
            for fname in filename:
                f_name = os.path.splitext(fname)[0]
                f_ext = os.path.splitext(fname)[1]
                if ext1 == f_ext:
                    c_name = os.path.join(Dirname,fname)
                    n_name = os.path.join(Dirname,f_name+ext2)

                    try:
                        os.rename(c_name,n_name)
                    except OSError as e:
                        print("An error occured :", e)

        print("File renamed successfully")

    else:
        print("Invalid Path Given")

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
            RenameFile(Directory, current_ext, new_ext)

        except ValueError:
            print("Invalid input datatype")
        except Exception as E:
            print("Error :", E)
    else:
        print("Invalid Number of Aurguments")

if __name__ == "__main__":
    main()