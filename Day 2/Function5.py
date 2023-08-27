#function accepts parameter and call another function from it

def Add(A,B):
    return A + B

def Sub(A,B):
    return A - B

def Marvellous(Value1,Value2):

    Ans = Add(Value1,Value2)
    print("Addition is :", Ans)

    Ans = Sub(Value1,Value2)
    print("Sunstraction is :", Ans)

def main():
    Marvellous(11,2)

if __name__ == "__main__":
    main()

