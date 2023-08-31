"""Design python application which creates two threads as evenlist and oddlist. both the threads accept list of integers
as parameter. Evenlist thread accpet all even elements and returns additions and oddlist thread accepts all odd elements
and return addition."""

import threading

def EvenList(L):
    Addition = sum(list(filter(lambda x : x % 2 == 0, L)))
    print("Addition of Even Numbers:",Addition)

def OddList(L):
    Addition = sum(list(filter(lambda x : x % 2 != 0, L)))
    print("Addition of Odd Numbers:",Addition)


def main():
    l1 = [1,2,3,4,5,6,7,8,9,10]

    thread_even = threading.Thread(target = EvenList, args =(l1,))
    thread_odd = threading.Thread(target = OddList, args =(l1,))

    thread_even.start()
    thread_odd.start()

    thread_even.join()
    thread_odd.join()


if __name__=="__main__":
    main()