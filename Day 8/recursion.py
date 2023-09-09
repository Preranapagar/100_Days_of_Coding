def DisplayW():

    no = 1
    while no < 6:
        print(no)
        no = no + 1

def DisplayF():
    for i in range(1,6):
        print(i)

def main():
    DisplayF()
    DisplayW()

if __name__=="__main__":
    main()