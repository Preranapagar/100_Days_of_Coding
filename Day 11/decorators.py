
print("Demonstration of Decorators")

def Sub(a,b):
    print(a-b)

def SmartSub(fptr): #define inner function which swaps the numbers depends on its value
    def inner(a,b):
        if a<b:
            a,b = b,a
        return fptr(a,b)
    return inner

def main():

    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))


    sub =SmartSub(Sub)
    sub(No1,No2)

if __name__=="__main__":
    main()

    