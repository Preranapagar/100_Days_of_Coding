#write a program which accepts number and returns its factorial
# ex. input =5, output = 120

def Factorial(Num):
    if Num == 1 :
        return 1
    else:
        return Num * Factorial(Num-1)
        
def main():

    Number = int(input("Enter the Number :"))
    Answer = Factorial(Number)
    print("Factorial of Number:",Answer)

if __name__ == "__main__":
    main()