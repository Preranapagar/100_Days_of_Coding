#write a program which accepts two file names from user and compare contains of both the files.
#if both the files contains same content then display success otherwise display failure. accept names of files from command line

import os
import sys

def main():

    argv = sys.argv
    if len(argv) < 3:
        print("Please enter the both file names as command line prompt")
    else:
        file1 = argv[1]
        file2 = argv[2]

        if os.path.exists(file1) and os.path.exists(file2):
            fobj = open(file1,'r')
            fobj2 = open(file2,'r')

            print(f"Opening {file1}.....")
            print(f"Opening {file2}.....")

            data1 = fobj.read()
            data2 = fobj2.read()

            if data1 == data2 :
                print("Success")
            else:
                print("Failure")

            fobj.close()
            fobj2.close()
        else:
            print("Files doesn't exist in your directory")
        

if __name__=="__main__":
    main()