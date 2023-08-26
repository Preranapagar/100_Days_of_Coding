#Function syntax

def Addition(No1,No2):
    Result = 0
    Result = No1 + No2
    return Result

Value1 = int(input("Enter first number:"))
Value2 = int(input("Enter second number:"))

Answer = Addition(Value1,Value2)
print("Answer is :", Answer)