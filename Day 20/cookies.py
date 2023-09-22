#You will be given list of childern with greed factor and list of cookies. you need to assign each child a cookie

def FindContentChildren(g,s):
    i = 0
    j = 0
    g = sorted(g)
    s = sorted(s)

    while i < len(g) and j <len(s):
        i += g[i] <= s[i]
        j =  j + 1

    return i

def main():

    g = [3,5,6,1,2]
    s = [1,1,4]

    print(FindContentChildren(g,s))

if __name__ == "__main__":
    main()
