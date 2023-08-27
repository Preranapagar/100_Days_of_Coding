
#Function defines another function in it (Inner function)

def Demo():
    def Add(A,B):
        return A + B
    return Add
    

def main():
    Arr =Demo()
    Ans = Arr(10,5)

    print("Addition is :", Ans)

if __name__ == "__main__":
    main()