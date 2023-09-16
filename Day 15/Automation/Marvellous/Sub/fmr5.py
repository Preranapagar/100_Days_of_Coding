import functools

check_even = lambda No:(No % 2 == 0)
    
increas = lambda No: (No + 2)

add = lambda a,b: (a + b)


def main():
    Len_of_list = int(input("Enter number of elements :"))

    Data = []
    for i in range(Len_of_list):
        Data.append(int(input()))

    print("Input List :",Data)

    output = list(filter(check_even,Data))
    print("Filter :",output)

    moutput = list(map(increas, output))
    print("Map :",moutput)

    soutput = functools.reduce(add,moutput)
    print("Reduce :",soutput)



if __name__ == "__main__":
    main()