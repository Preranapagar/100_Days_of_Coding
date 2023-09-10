#write recursive program to print below pattern
#input:5 ,output: 5 4 3 2 1

def Display(No):
    if No >= 1:
        print(No, end= ' ')
        No -= 1
        Display(No)


def main():
    No = int(input("Enter the Number :"))
    Display(No)

if __name__ == "__main__":
    main()