#Automation script which accept directory name from user and display all names of duplicate  files from that directory

from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups={}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(filen)
                else:
                    dups[file_hash]=[filen]
        return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results)>0:
        print("Duplicates found :")

        for result in results:
            print("Following files are identical :")
            for subresult in result:
                print(subresult)
            print()
        
        print("Following files are duplicate :")
        for result in results:
            icnt = 0
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print('\t\t%s'%subresult)
    else:
        print("No duplicate files found.")

def main():
    print("_____________________________New Application_____________________________")
    print("Application name :"+argv[0])

    if len(argv) != 2:
        print("Error : Invalid number of aurguments")
        exit()

    if (argv[1]=='-h') or (argv[1]=='-H'):
        print("This script is use to traverse specific directory and display sizes of files")
        exit()

    if (argv[1]=='-u') or (argv[1]=='-U'):
        print("Usage : ApplicationName AbsolutePath_of_Directory_extension")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of input")

if __name__ == "__main__":
    main()


