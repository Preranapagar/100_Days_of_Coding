
import MathOp

def main():
    Value1 = int(input("Enter first number :"))
    Value2 = int(input("Enter second number :"))

    Result = MathOp.Addition(Value1,Value2)
    print(Result)

    Result = MathOp.Substraction(Value1,Value2)
    print(Result)

    Result = MathOp.Multiplication(Value1,Value2)
    print(Result)

    Result = MathOp.Division(Value1,Value2)
    print(Result)

if __name__ == "__main__":
    main()