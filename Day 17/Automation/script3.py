#remove duplicate files using script

from sys import *
import os
import hashlib


def hashfile(path, blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buffer = afile.read(blocksize)

    while len(buffer)>0:
        hasher.update(buffer)
        buffer = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def Checkdups(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    
    exist = os.path.isdir(path)
    if exist:
        dups = {}
        for dirname, subdirname, filename in os.walk(path):
            for file in filename:
                f_path = os.path.join(dirname,file)
                hash_file = hashfile(f_path)
                
                if hash_file in dups:
                    dups[hash_file].append(f_path)
                else:
                    dups[hash_file]=[f_path]
        return dups
    else:
        print("Invalid Path")

def RemoveDups(dict1):
    results = list(filter(lambda x : len(x)>1, dict1.values()))

    if len(results)>0:
        print("Duplicates found")
        print()
        for result in results:
            print("Below files are identical :")
            for sub in result:
                print(sub)
            print()


        for result in results:
            count = 0
        
            for sub in result:
                count +=1
                if count > 1:
                    print(f"to be removed....{sub}")
                    
                    os.remove(sub)

    else:
        print("No duplicates found")


def main():
    print("--------------------------Automation Script--------------------------")
    print("Script Name :", argv[0])

    if len(argv)==2:
        if argv[1]=='-h' or argv[1]=='-H':
            print("This script is use to remove duplicate file in given directory")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("Usage : Application_Name Absolute_Path_of_Directory")
            print("Example : Script.py Demo")
            exit()

    if len(argv) !=2:
        print("Invalid number of arguments")
    else:
        arr=Checkdups(argv[1])
        RemoveDups(arr)

if __name__=="__main__":
    main()