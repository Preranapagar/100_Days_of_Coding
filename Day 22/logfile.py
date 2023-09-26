
def MyFunction():
    result = 'This is my function'

    fobj = open('result.log','w')
    fobj.write(result)
    fobj.close()

    print("Operation Successful")

def main():
    MyFunction()

if __name__=="__main__":
    main()