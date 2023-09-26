from sys import *

def MyFunction():
    result = 'This is my function'
    name = f"{argv[1]}.log"
    fobj = open(name,'w')
    fobj.write(result)
    fobj.close()

    print("Operation Successful")

def main():
    MyFunction()

if __name__=="__main__":
    main()