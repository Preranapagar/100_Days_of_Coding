from sys import *
from Module import *
import schedule 
import time
from Mail import *
#Script

def main():
    print("Automation Script Name :", argv[0])

    if len(argv)==2:
        if argv[1]=='-h' or argv[1]== '-H':
            print("""This script accepts the directory name from user and delete duplicate files from that directory as well as mail log file of deleted files to the provided email""")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("Usage : Script_name First_argument Second_argument")
            print("Example : script.py Demo user@gmail.com")
            exit()

    if len(argv) !=4:
        print("Invalid Number of Auguments")
        exit()

    else:
        try:
            directory = argv[1]
            schedule_time = int(argv[2])
            receiver_mail = argv[3]

            def my_fun():
                scanning_time = time.ctime()
                dicts = Check_Sum(directory)
                deleted = Delete_Duplicate(dicts[0],dicts[1])
                path = Create_Log(deleted)

                count = [len(dicts[1]),len(deleted)]


                if is_connected():
                    MailSender(path,receiver_mail,time.ctime(),scanning_time,count)

            my_fun()
            schedule.every(schedule_time).minutes.do(my_fun)
            while True:
                schedule.run_pending()
                time.sleep(1)

        except ValueError:
            print("Invalid datatype of input")

        except Exception as E:
            print("Error :", E)

if __name__=="__main__":
    main()