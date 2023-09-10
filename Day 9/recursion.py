
#write a recursive program which displays below pattern
# input = 5 output = * * * * *

i = 1

def Display(No):
    global i
    if i <= No:
        print('*', end =' ')
        i += 1
        Display(No)

def main():
    No = int(input("Enter the number :"))
    Display(No)

if __name__ == "__main__":
    main()

