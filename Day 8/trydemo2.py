def main():

    try:
        print("Enter First Number :")
        No1 = int(input())

        print("Enter Second Number :")
        No2 = int(input())

        Ans = 0
        Ans = No1 / No2

    except ZeroDivisionError as zobj:
        print("Divide by zero is not allowed :", zobj)
        return
    
    except ValueError as obj:
        print("Invalid input :", obj)
        return
    
    except Exception as zobj:
        print("Error :", zobj)
        return

    print("Division is :", Ans)

if __name__=="__main__":
    main()