
#Binary search algorithm : algorithm to find an element in a sorted array by repeatedly dividing the search interval in half.

#input =[-1,0,3,5,9,12], target = 9, output = 4

def Binary_Search(nums,target):

    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low + high) //2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():

    List = [-1,0,3,5,9,12]
    target = int(input("Enter your target :"))

    print(Binary_Search(List,target))

if __name__=="__main__":
    main()