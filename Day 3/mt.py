"""Design python application which creates two thread as even and odd. even thread will display first 10 even numbers and odd thread 
will display first 10 odd numbers"""

import threading


def EvenNum(Num):
    for i in range(Num):
        if i % 2 == 0:
            print("Even Num :", i)

def OddNum(Num):
    for i in range(Num):
        if i % 2 != 0:
            print("Odd Num :", i)

def main():
    No = 20

    t1 = threading.Thread(target = EvenNum, args = (No,))
    t2 = threading.Thread(target = OddNum, args = (No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()