#detect capital in word and return true 
# all the letters are uppercase : return true
# all the letters are lowercase : return true
# only the first letter is capital : return true
# some letters are upper and some are lower : return false
# first letter is lowercase and remaining upper case : return false

def Detect_Capital(word):
    if word.isupper() or word.islower() or word.istitle():
        return True
    else:
        return False
    
def main():
    string = input("Enter Your Word:")
    Answer = Detect_Capital(string)

    print(Answer)
    
if __name__=="__main__":
    main()    