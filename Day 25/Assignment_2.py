#Design automation script which accept process name from user and display information of process if its running
from pinfo import *
from sys import *

def main():
    print("Automation Script:", argv[0])
    
    if len(argv)==2:
        if argv[1]=='-h' or argv[1]=='-H':
            print("This script use to display information of processes if its running")
            exit()

        elif argv[1]=='-u' or argv[1]=='-U':
            print("Usage : Script_Name Process_Name")
            print("Example : Script_name.py Process")

        else:
            process = ProcessDisplay()

            for i in range(len(process)):
                if argv[1] == process[i]['name']:
                    print("Given process is running :", process[i])
                    break
            else:
                print("Given process is not running")
    else:
        print("Invalid Number of Aurguments")


if __name__=="__main__":
    main()

