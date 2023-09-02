from functools import reduce

def New_Fun(a,b):
    return a + b

def main():
    list1 = [1,2,3,4,5]

    new_list = reduce(New_Fun,list1)

    print(new_list)

if __name__=="__main__":
    main()