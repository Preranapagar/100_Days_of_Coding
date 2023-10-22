#What is race condition ?
# Ans : A race condiyion occures when two or more threads can access shared data and try to change it at the same time.
# The result of the change depends on the timing of how the thread run

import threading

counter = 0

def increment():
    global counter
    for i in range(1000000):
        counter += 1

def main():
    thread1 = threading.Thread(target= increment)
    thread2 = threading.Thread(target = increment)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(counter)

if __name__=="__main__":
    main()
