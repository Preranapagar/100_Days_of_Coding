#you wil be given an array of positive intgers with some elements missing or duplicated, identify and return them
# ex. Input : [1,2,3,4,4,6] Output:[5,4]

def Mismatched(nums):

    n = len(nums)

    duplicate = -1
    for num in nums:
        if nums[abs(num)-1]<0:
            duplicate = abs(num)
        else:
            nums[abs(num)-1]*=-1

    missing = -1
    for i in range(n):
        if nums[i]>0:
            missing = i + 1

    return [missing, duplicate]
    

def main():

    L1 = [1,2,3,4,4,5]

    Answer = Mismatched(L1)
    print(Answer)

if __name__=="__main__":
    main()