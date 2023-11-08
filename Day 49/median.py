
def median(list1,list2):
    list1.extend(list2)
    list1.sort()

    l = len(list1)

    if l%2==0:
        median = (list1[int(l/2)] + list1[int(l/2)-1])/2
        return median
    else:
        median = list1[int(l/2)]
        return median
    
def main():

    arr = [1,2]
    arr2 = [3,4]

    answer = median(arr,arr2)
    print(answer)

if __name__=="__main__":
    main()
