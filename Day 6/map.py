
def Increase(No):
    return No + 5

def main():
    list_1 = [1,2,3,4,5]
    new_list = list(map(Increase,list_1))
    print(new_list)

if __name__=="__main__":
    main()