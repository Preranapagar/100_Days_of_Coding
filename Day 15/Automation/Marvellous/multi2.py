
import threading
import os

def Fun(Value):
    print("Fun:")
    print("PID of Fun:", os.getpid())

def Gun(Value):
    print("Gun:")
    print("PID of Gun:", os.getpid())


def main():
    print("PID of parent prcoess is :", os.getpid())
    No = 5

    t1 = threading.Thread(target = Fun, args =(No,))
    t2 = threading.Thread(target = Gun, args =(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()