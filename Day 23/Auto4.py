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