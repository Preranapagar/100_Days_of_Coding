#check even number using filter

def CheckEeven(No):
    if No % 2 == 0:
        return True
    else:
        return False
    
def main():
    List = [1,2,3,4,5,6,7,8,9]
    new_list = list(filter(CheckEeven, List))
    print(new_list)

if __name__=="__main__":
    main()
    