
#inbult function (we cannot modify the contents)
def Sub(a,b):
    return a-b

#decorator

def SmartSub(FTPR):
    def Inner(a,b):
        if a<b:
            a,b=b,a
        return FTPR(a,b)
    return Inner

def main():
    SubX = SmartSub(Sub)

    Ret = SubX(10,3)
    print("Substraction is:", Ret)

    Ret = SubX(3,10)
    print("Substraction is:", Ret)

if __name__=="__main__":
    main()