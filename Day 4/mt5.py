"""Design python application which creates three threads as small, cpaital and digits. all the three accepts string
as parameter. small thread displays number of small characters, capital thread displays number of capital characters
, digit thread displays number of digits. display ID and name of each thread."""

import threading

def Capital_count(string):
    count = 0
    for i in string:
        if i.isupper()==True:
            count +=1

    print("Count of capital characters in string :", count)
    print("thread ID of current thread is :", threading.current_thread())
    print("thread name of current thread is :", threading.current_thread().name)

def Lower_count(string):
    count = 0
    for i in string:
        if i.islower()==True:
            count +=1
    print("Count of lower character in string :", count)
    print("thread ID of current thread is :", threading.current_thread())
    print("thread name of current thread is :", threading.current_thread().name)

def Digit_count(string):
    count = 0
    for i in string:
        if i.isdecimal()==True:
            count +=1
    print("Count of digits in string :", count)
    print("thread ID of current thread is :", threading.current_thread())
    print("thread name of current thread is :", threading.current_thread().name)

def main():

    string = input("Enter your string:")

    threadA = threading.Thread(target = Capital_count, args = (string,))
    threadB = threading.Thread(target = Lower_count, args = (string,))
    threadC = threading.Thread(target = Digit_count, args =(string,))

    threadA.start()
    threadB.start()
    threadC.start()

    threadA.join()
    threadB.join()
    threadC.join()

if __name__=="__main__":
    main()