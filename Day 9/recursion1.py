#Write recursive program which displays below pattern
#Input : 5, output: 1 2 3 4 5 

i = 1

def Display(No):
    global i

    if i <= No:
        print(i, end=' ')
        i += 1
        Display(No)

def main():

    No = int(input("Enter the Number :"))

    Display(No)

if __name__ == "__main__":
    main()