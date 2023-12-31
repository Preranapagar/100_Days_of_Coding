import psutil
import os
import datetime as ds
import time

def ProcessDisplay():
    #Create a list of running processess
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

def CreateLog(process_list,log_dir = "Process_log"):
    #create a log of running process
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    current_time = ds.datetime.now()
    timestamp = current_time.strftime('%d_%b_%y-%H-%M-%S')

    seperator = '-'*80

    log_path = os.path.join(log_dir,"%sLog_%s.log"%(log_dir,timestamp))
    log = open(log_path,'w')
    log.write(seperator+'\n')
    log.write("Process Logger :"+time.ctime()+'\n')
    log.write(seperator+'\n')

    for ele in process_list:
        log.write('%s\n'%ele)

    log.close()
    print("Log created")

    
