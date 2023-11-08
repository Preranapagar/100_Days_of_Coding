#Python program to print pascal triangle
from math import factorial

def pascal_triangle(num):
    
    for i in range(num+1):
        for j in range(num-i+1):
            print(end=' ')

        for k in range(i+1):
            ele = factorial(i)/(factorial(k)*factorial(i-k))
            print(int(ele),end=' ')
        print()

def main():
    n = int(input("Enter number of rows :"))
    pascal_triangle(n)

if __name__=="__main__":
    main()