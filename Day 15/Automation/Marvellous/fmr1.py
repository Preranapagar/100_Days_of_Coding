import functools

def check_even(No):
    if No % 2 == 0:
        return True
    else:
        return False
    
def increas(No):
    return No + 2

def add(a,b):
    return a + b


def main():
    Data = [5,4,9,8,13,17,12,18]
    print(Data)
    output = list(filter(check_even,Data))
    print(output)

    mouput = list(map(increas, output))
    print(mouput)

    soutput = functools.reduce(add,mouput)
    print(soutput)



if __name__ == "__main__":
    main()