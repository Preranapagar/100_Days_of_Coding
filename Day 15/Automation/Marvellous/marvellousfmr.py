
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