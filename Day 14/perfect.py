
#check if given number id perfect number or not

def FindingPerfect(Num):
    Factors = [i for i in range(1,Num-1) if (Num % i)==0 ]

    if sum(Factors) == Num:
        return True
    else:
        return False
    
def main():

    No = int(input("Enter the number to check :"))

    Ans = FindingPerfect(No)
    print(Ans)

if __name__ == "__main__":
    main()