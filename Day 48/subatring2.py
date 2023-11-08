#find the length of longest substring without repeating character

def lengthoflongestsubstring(string):
    if len(string)==0:
        return 0
    maxans = -1
    for i in range(len(string)):
        set = {}

        for j in range(i,len(string)):
            if string[j] in set:
                maxans = max(maxans, j-i)
                break
            set[string[j]]=1
    return maxans

def main():
    str1 = input("Enter your string :")

    ans = lengthoflongestsubstring(str1)
    print(ans)

if __name__=="__main__":
    main()