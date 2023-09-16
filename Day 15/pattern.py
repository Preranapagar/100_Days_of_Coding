#you will be given a string and you have to find out if a given string can be formed by repeating a substring
#ex, Input :'abab' Output:True

def RepeatedString(String):
    n = len(String)
    if String[:(n//2)] == String[n//2:]:
        return True
    else:
        return False
    
def main():

    data = input("Enter Your String :")
    answer = RepeatedString(data)

    print(answer)

if __name__=="__main__":
    main()