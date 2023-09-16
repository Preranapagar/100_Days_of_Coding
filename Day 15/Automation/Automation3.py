from sys import *
from Arithmatic import *

def main():
    print("_______________Automation Script_______________")
    print("Automation Script Name :", argv[0])

    if (len(argv)==2):
        if (argv[1] == "-h" or argv[1]== "-H"): #flag for displaying help
            print("This automation script is used to perform addition of two  numbers")
            exit()

        elif (argv[1] == "-u" or argv[1]=="-U"): #flag displaying the usage of script
            print("Usage : Name_of_script First_Argument Second_Argument")
            print("Example : Demo.py 11 10")
            exit()

        else:
            print("There is no such optionn to handle")

    if(len(argv) !=3):
        print("Invalid Number of Aurguments")
        exit()

    else:
        Result = Addition(int(argv[1]),int(argv[2]))
        print("Addition is :", Result)
        


if __name__=="__main__":
    main()