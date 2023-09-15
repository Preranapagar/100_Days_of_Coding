#check perfect number using while loop

def CheckPerfect(Num):
    if Num <= 1:
        return False
    
    div_sum = 1
    i = 2

    while i*i <= Num:
        
        if Num % i == 0:
            div_sum += i
            if i != Num//i:
                div_sum += Num//i
                print("sum :", div_sum)
            
    
        i += 1

    if div_sum == Num:
        return True
    else:
        return False
    
def main():

    No = int(input("Enter the number to check :"))

    Answer = CheckPerfect(No)
    print(Answer)

if __name__=="__main__":
    main()
    

