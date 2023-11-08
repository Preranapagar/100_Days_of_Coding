
def longestpalindromesubstring(string):
    palindrome = {}

    for i in range(len(string)):
        for j in range(i,len(string)):
            ns = string[i:j+1]
            if ns==ns[::-1]:
                palindrome[len(ns)]=ns
    return palindrome[max(list(palindrome.keys()))]

def main():

    string = 'dhkabdlrgababdswa'
    answ = longestpalindromesubstring(string)
    print(answ)
    
if __name__=="__main__":
    main()