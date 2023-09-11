#accept file name and one string from user and return the frequency of that string from file
import os

def main():
    file_name = input("Enter the file name :")

    if os.path.exists(file_name):
        string = input("Enter your string :")

        fobj = open(file_name,'r')
        data = fobj.read()

        count = 0
        for i in data.split():
        
            if i == string:
                count +=1
        print(f"frequency of '{string}' in {file_name} is {count}")
    
    else:
        print("File doesn't exist in current directory")


if __name__=="__main__":
    main()