"""Python application which contains two threads named as thread1 and thread2, thread 1 displays 1 to 50 and thread2 displays 50 to 1.
after completion of thread1 schedule thread 2"""

import threading

def Display(Num):
    for i in range(1,Num+1):
        print(i)

def Display_Reverse(Num):
    while Num > 0:
        print(Num)
        Num = Num - 1

def main():

    No = 50

    thread1 = threading.Thread(target = Display, args = (No,))
    thread2 = threading.Thread(target = Display_Reverse, args = (No,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__=="__main__":
    main()