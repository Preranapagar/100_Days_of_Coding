#check if two strings different from exactly a swap of two letters. if such a swap exists, the program should return true;
#otherwise, it should return false. The program should also return false if two strings have different lengths

#input = 'ab','ba' , output = True

def BuddyString(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        l1 = [i for i in s1]
        l2 = [i for i in s2]

        if sorted(l1) == sorted(l2):
            return True
        else:
            return False

    
def main():

    string_1 = input("Enter first string :")
    string_2 = input("Enter second string :")


    Answer = BuddyString(string_1,string_2)
    print("Given Strings are Buddy String :", Answer)

if __name__=="__main__":
    main()