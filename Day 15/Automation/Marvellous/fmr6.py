import functools

def main():
    Len_of_list = int(input("Enter number of elements :"))

    Data = []
    for i in range(Len_of_list):
        Data.append(int(input()))

    print("Input List :",Data)

    output = list(filter(lambda No:(No % 2 == 0),Data))
    print("Filter :",output)

    moutput = list(map(lambda No: (No + 2), output))
    print("Map :",moutput)

    soutput = functools.reduce(lambda a,b: (a + b),moutput)
    print("Reduce :",soutput)

if __name__ == "__main__":
    main()


    # soutput = functools.reduce(lambda a,b: (a + b),list(map(lambda No: (No + 2), list(filter(lambda No:(No % 2 == 0),Data)))))
    # print("Reduce :",soutput)