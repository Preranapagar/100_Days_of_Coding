from sys import *

def main():
    print("_______________Automation Script_______________")

    if (argv[1] == "-h"): #flag for displaying help
        print("This automation script is used to perform addition of two  numbers")
        exit()

    if (argv[1] == "-u"): #flag displaying the usage of script
        print("Usage : Name_of_script First_Argument Second_Argument")
        print("Example : Demo.py 11 10")
        exit()

if __name__=="__main__":
    main()