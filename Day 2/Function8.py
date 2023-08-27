
#Function defines another function in it (Inner function)

def Demo(Value1,Value2):
    def Add(A,B):
        return A + B
    
    Ans = Add(Value1,Value2)
    return Ans
    

def main():
    Arr =Demo(11,2)

    print("Addition is :", Arr)

if __name__ == "__main__":
    main()