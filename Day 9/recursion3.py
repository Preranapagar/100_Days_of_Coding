#write a recursive program which accepts number and returns summation of its digits
#ex. input: 879, Output:24

def Sum_Digit(Num):
    if Num < 10:
        return Num
    else:
        last_digit = Num % 10
        remaining = Num // 10
        return last_digit + Sum_Digit(remaining)
    
def main():

    No = int(input("Enter the Number :"))

    Answer = Sum_Digit(No)
    print("Summation of all digits of number is :", Answer)

if __name__ == "__main__":
    main()