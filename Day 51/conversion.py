
def myatoi(s):
    ans = ''
    s = s.strip()
    for i in s:
        if i=='-' or i=='+':
            ans += i
        elif i.isdecimal():
            ans += i
        else:
            if len(ans)==0:
                ans += '0'
                break
            else:
                break
    print(int(ans))

if __name__=="__main__":
    s1 = '42'
    s2 = '-42'
    s3 = '       65 word'
    s4 = 'word 65'
    myatoi(s1)
    myatoi(s2)
    myatoi(s3)
    myatoi(s4)