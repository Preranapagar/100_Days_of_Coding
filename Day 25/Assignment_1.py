#Automation script which create log to display information of running processes

from sys import *
import pinfo

def main():
    print("Automation Script to Display running process information")

    running_process = pinfo.ProcessDisplay()

    if len(argv) == 1:
        pinfo.CreateLog(running_process)
    elif len(argv) == 2:
        pinfo.CreateLog(running_process,argv[1])
    else:
        print("Invalid Number of Aurguments")

if __name__ == "__main__":
    main()

