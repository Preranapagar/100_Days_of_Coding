#Libraries :
import os
import hashlib
import datetime as ds

#Functions :
def Hashfile(path, blocksize =1024):
    hasher = hashlib.md5()
    f = open(path,'rb')
    buf = f.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = f.read(blocksize)

    return hasher.hexdigest()


def Check_Sum(dirname):
    print("Scanning through directory :", dirname)
    flag = os.path.isabs(dirname)
    if flag == False:
        dirname = os.path.abspath(dirname)

    exist = os.path.isdir(dirname)
    
    CheckList = {}
    FilePath = {}

    if exist:
        for Dirname, Foldername, Filename in os.walk(dirname):
            for file in Filename:
                f_path = os.path.join(Dirname,file)
                checksum = Hashfile(f_path)
                FilePath[file]=f_path

                if checksum in CheckList:
                    CheckList[checksum].append(file)
                else:
                    CheckList[checksum]=[file]

        return CheckList,FilePath
    else:
        print("Invalid Directory Path")
        exit()

def Create_Log(l,dir="Marvellous"):
    if not os.path.exists(dir):
        os.mkdir(dir)

    current_time = ds.datetime.now()
    time_stamp = current_time.strftime('%d-%b-%y_%H-%M-%S')

    log_path = os.path.join(dir,'Log_%s.log'%(time_stamp))
    log = open(log_path,'w')

    seperator = '-'*80
    log.write(seperator+'\n')
    log.write('Log of deleted file at : %s \n'%(time_stamp))
    log.write(seperator+'\n')

    for ele in l:
        log.write('%s\n'%ele)

    print("Log file generated")
    return log_path

def Delete_Duplicate(dict1,dict2):
    results = list(filter(lambda x : len(x)>1, dict1.values()))
    deleted = []
    if len(results)>=1:
        for dups in results:
            for i in range(1,len(dups)):
                deleted.append(dups[i])
                path = dict2[dups[i]]
                os.remove(path)
        print("Duplicate files are removed")
        
        return deleted

    else:
        print("No Duplicate files found in given directory")
        return deleted



    

