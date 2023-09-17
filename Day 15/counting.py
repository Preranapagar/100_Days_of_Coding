""" You will be given an integer n. to solve this problem, return an array of length n+1 where the elements
will be number of 1's present in the binary representation of the index number of each value in the array"""

#ex. Input: 5, Output : [0,1,1,2,1,2]

def CountBits(num):
    counter = [0]

    if num >= 1:
        while len(counter) <= num :
            counter = counter + [i + 1 for i in counter]
        return counter [:num+1]
    else:
        return 0
    
def main():

    No = int(input("Enter Your Number :"))
    Ans = CountBits(No)

    print("Bits count :", Ans)

if __name__=="__main__":
    main()