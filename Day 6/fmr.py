#Design your own filter, map and reduce function

#Task : Function
#Element : List of data elements

def filterX(Task, Element):
    Result = []
    for i in Element:
        if Task(i)==True:
            Result.append(i)
    return Result

def mapX(Task, Element):
    Result = []
    for i in Element:
        Ret = Task(i)
        Result.append(Ret)
    return Result

def reduceX(Task, Element):
    Result = 1
    for i in Element:
        Result = Task(Result, i)
    return Result

#Function 
CheckEven = lambda x : x % 2 == 0
DivideNum = lambda x : x / 2
MultiplyNum = lambda x, y : x * y

def main():

    Data = []
    length = int(input("Enter the number of elements:"))

    for i in range(length):
        Data.append(int(input(f"Enter {i}st element:")))
    
    print("Given List :", Data)

    Output_1 = list(filterX(CheckEven, Data))
    print("Filterred Output :", Output_1)

    Output_2 = list(mapX(DivideNum, Output_1))
    print("Divided Output :", Output_2)

    Output_3 = reduceX(MultiplyNum, Output_2)
    print("Final Output:", Output_3)

if __name__=="__main__":
    main()