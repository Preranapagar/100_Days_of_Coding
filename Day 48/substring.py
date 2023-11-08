#find the length of longest substring without repeating character

def lengthoflongestsubstring(string):
    longest_string = ''

    for i in range(len(string)):
        for j in range(i,len(string)):
            ns = string[i:j+1]
            st = set()
            for k in ns:
                st.add(k)
            if len(ns)==len(st):
                if len(ns)>len(longest_string):
                    longest_string = ns

    print("Longest string is :", longest_string)
    print("Length of longest string is :", len(longest_string))

def main():
    str1 = input("Enter your string :")
    lengthoflongestsubstring(str1)

if __name__=="__main__":
    main()