import marvellousfmr as mfmr

check_even = lambda No:(No % 2 == 0)   
increas = lambda No: (No + 2)
add = lambda a,b: (a + b)


def main():
    Len_of_list = int(input("Enter number of elements :"))

    Data = []
    for i in range(Len_of_list):
        Data.append(int(input()))

    print("Input List :",Data)

    output = list(mfmr.filterX(check_even,Data))
    print("Filter :",output)

    moutput = list(mfmr.mapX(increas, output))
    print("Map :",moutput)

    soutput = mfmr.reduceX(add,moutput)
    print("Reduce :",soutput)



if __name__ == "__main__":
    main()