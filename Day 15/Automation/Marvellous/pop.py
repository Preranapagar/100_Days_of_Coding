def Add(No1,No2):
    return No1 + No2

def Sub(No1,No2):
    return No1 - No2

def main():

    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))

    Ret =Add(Value1, Value2)
    print("Addition :", Ret)

    Ret =Sub(Value1, Value2)
    print("Substraction:", Ret)


if __name__ == "__main__":
    main()