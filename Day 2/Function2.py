#Function accepts parameter returns parameter
#Function to return largest number from two

def Marvellous(Value1,Value2):
    if(Value1 > Value2):
        return Value1
    else:
        return Value2
    
def main():

    Ret = Marvellous(34,67)
    print("Largest number is :", Ret)

    Ret = Marvellous(65,23)
    print("Largest number is :", Ret)

if __name__ == "__main__":
    main()