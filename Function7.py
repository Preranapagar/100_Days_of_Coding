#function accepts parameter as another function

def Add(A,B):
    return A + B

def Sub(A,B):
    return A - B

def Marvellous(FPTR1, FPTR2):
    Ans = FPTR1(10,4)
    print("Addition is :", Ans)

    Ans = FPTR2(10,4)
    print("Substraction is :", Ans)

def main():
    Marvellous(Add,Sub)

if __name__ == "__main__":
    main()