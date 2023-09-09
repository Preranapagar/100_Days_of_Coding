import sys

def main():
    print("Recursion Limit :", sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("Recursion Limit :", sys.getrecursionlimit())



if __name__=="__main__":
    main()