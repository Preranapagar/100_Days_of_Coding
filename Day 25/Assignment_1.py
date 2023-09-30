#Automation script which create log to display information of running processes

from sys import *
import pinfo

def main():
    print("Automation Script :"+argv[0])
    running_process = pinfo.ProcessDisplay()

    if len(argv) == 1:
        pinfo.CreateLog(running_process)

    if len(argv) == 2:
        if argv[1]=='-h' or argv[1]=='-H':
            print("This script use to display information of running processes")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("to create Default log file")
            print("Example : Script_name.py")
            print('-'*50)
            print("to create log file with user given name")
            print("Example : script_name.py Demo")
            exit()

        else:
            pinfo.CreateLog(running_process,argv[1])
    
    else:
        print("Invalid Number of Aurguments")

if __name__ == "__main__":
    main()

