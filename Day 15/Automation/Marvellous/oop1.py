
class Arithmetic:
    def __init__(self, A, B):
        print("Inside Constructor")
        self.No1 = A
        self.No2 = B
    
    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans= 0
        Ans = self.No1 - self.No2
        return Ans


def main():

    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))

    obj1 = Arithmetic(Value1, Value2)

    Ret = obj1.Addition()
    print("Addition:", Ret)

    Ret = obj1.Substraction()
    print("Subtraction :", Ret)

    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))

    obj2 = Arithmetic(Value1, Value2)

    Ret = obj2.Addition()
    print("Addition:", Ret)

    Ret = obj2  .Substraction()
    print("Subtraction :", Ret)



if __name__ == "__main__":
    main()