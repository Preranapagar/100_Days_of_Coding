
"""Design python application which creates two threads as evenfactor and oddfactor. both the thread accepts one parameter as integer.
evenfactor thread will display addition of even factors of number and oddfactor thread will display addition of odd factors of number.
after execution of both thread completed main thread should display message as 'exit from main'"""

import threading

def EvenFactor(Num):
    Sum = 0
    for i in range(1,Num+1):
        if Num % i == 0 and i % 2 == 0:
            Sum = Sum + i

    print("Sum of Even Factors of Number :", Sum)

def OddFactor(Num):
    Sum = 0
    for i in range(1,Num+1):
        if Num % i == 0 and i % 2 != 0:
            Sum = Sum + i

    print("Sum of Odd Factors of Number :", Sum)

def main():

    No = int(input("Enter the Number :"))

    thread1 = threading.Thread(target = EvenFactor, args = (No,))
    thread2 = threading.Thread(target = OddFactor, args = (No,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("exit from main")

if __name__=="__main__":
    main()