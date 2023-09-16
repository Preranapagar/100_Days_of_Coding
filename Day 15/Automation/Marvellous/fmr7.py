
check_even = lambda No:(No % 2 == 0)   
increas = lambda No: (No + 2)
add = lambda a,b: (a + b)

#Task = Name of Function
#Elements = List of data elements
def filterX(Task,Elements):
    Result = []
    for no in Elements:
        if Task(no)==True:
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result = []
    for no in Elements:
        Result.append(Task(no))
    return Result

def reduceX(Task,Elements):
    Result = 0
    for no in Elements:
        Result = Task(Result, no)
    return Result


def main():
    Len_of_list = int(input("Enter number of elements :"))

    Data = []
    for i in range(Len_of_list):
        Data.append(int(input()))

    print("Input List :",Data)

    output = list(filterX(check_even,Data))
    print("Filter :",output)

    moutput = list(mapX(increas, output))
    print("Map :",moutput)

    soutput = reduceX(add,moutput)
    print("Reduce :",soutput)



if __name__ == "__main__":
    main()