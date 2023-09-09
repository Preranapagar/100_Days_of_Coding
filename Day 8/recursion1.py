
i = 0

def DisplayF():
    global i
    print("Inside Function :", i)
    i += 1
    DisplayF()

def main():
    DisplayF()
    

if __name__=="__main__":
    main()