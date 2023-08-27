#Function accept multiple parameter and returns multiple parameter

def Marvellous(Value1, Value2):
    Addition = Value1 + Value2
    Substraction = Value1 - Value2
    Multiplication = Value1 * Value2

    return Addition , Substraction , Multiplication

def main():
    Ret1, Ret2, Ret3 = Marvellous(3,4)

    print("Addition is :", Ret1)
    print("Substraction is :", Ret2)
    print("Multiplication is :", Ret3)

if __name__ == "__main__":
    main()