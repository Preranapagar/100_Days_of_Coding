import multiprocessing
import os

def main():

    print("Number of cores :", multiprocessing.cpu_count())
    print("PID of current process is :", os.getpid())
    print("PID of parent process is :", os.getppid())

if __name__ == "__main__":
    main()