#validate if number is perfect square or not

def Perfect_Square(num):

    for i in range(1,num//2):
        if i * i == num :
            return True
            break
    else:
        return False
        
def main():
    Number = int(input("Enter the Number :"))

    Result = Perfect_Square(Number)
    print("Is the given number is perfect square :",Result)

if __name__ == "__main__":
    main()
