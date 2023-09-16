#you will be given a string and you have to find out if a given string can be formed by repeating a substring
#ex, Input :'abab' Output:True

def RepeatedSubstring(s):
    string = (s+s)[1:-1]
    return string.find(s) !=-1


def main():
    data =input("Enter the string :")

    Result = RepeatedSubstring(data)
    print(Result)

if __name__=="__main__":
    main()