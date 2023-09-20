
#find the first unique character of given string and give its index

def UniqueCharacter(str1):

    count = 0
    for i in str1:
        if str1.count(i)==1:
            print(f"the {i} is first unique character of string at index {str1.index(i)}")
            break
    else:
        print("no unique character in string")

def main():

    string = input("Enter your string :")
    UniqueCharacter(string)

if __name__=="__main__":
    main()

