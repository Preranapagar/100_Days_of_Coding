#Python program to print pascal triangle

def pascal_triangle(num_rows):

    for i in range(num_rows):
        print(" " * (num_rows-i), end='')
        print(' '.join(str(11**i)))

def main():
    no = int(input("Enter the number of rows :"))

    pascal_triangle(no)

if __name__=="__main__":
    main()