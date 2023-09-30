import psutil
import os

def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

def CreateLog(process_list,log_dir = "Process_log"):
    
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    
