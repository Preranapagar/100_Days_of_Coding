import threading
import os

def Task1(Value):
    print("Task 1:")
    print("PID of Task1")

def Task2(Value):
    print("Task 2:")


def main():
    print("Demonstartion of Threading")


    t1 = threading.Thread(target= Task1, args=(2,))
    t2 = threading.Thread(target= Task2, args=(3,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()