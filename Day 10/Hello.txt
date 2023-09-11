#write a which accepts file name from user and check whether that file exists in current directory or not.

import os

def main():
    File_name = input("Enter the file name to check :")

    if os.path.exists(File_name):
        print("Yes, your file exists in current directory")

    else:
        print("Your file doesn't exists in current directory")

if __name__ == "__main__":
    main()
