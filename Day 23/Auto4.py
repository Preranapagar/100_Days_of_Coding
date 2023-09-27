#create log file for duplicates from directory as well as delete duplicates
from sys import *
import os
import hashlib

def Hashfile(path,blocksize=1024):
    obj = open(path,'rb')
    hasher = hashlib.md5()
    buf = obj.read(blocksize)

    while len(buf)>1:
        hasher.update(buf)
        buf = obj.read(blocksize)

    obj.close()
    return hasher.hexdigest()

def CheckSum(dir):
    print("Scanning Directory :", dir)

    flag = os.path.isabs(dir)
    if flag == False:
        dir = os.path.abspath(dir)

    dups = {}
    file_paths = {}

    exist = os.path.isdir(dir)
    if exist:
        for Dirname, Foldername, Filename in os.walk(dir):
            for file in Filename:
                f_path = os.path.join(Dirname,file)
                file_paths[file]=f_path
                checksum = Hashfile(f_path)
                if checksum in dups:
                    dups[checksum].append(file)
                else:
                    dups[checksum]=[file]
        return dups, file_paths
    else:
        print("Invalid Directory Path")