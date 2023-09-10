import os

def main():
    print("Enter the name of file that your want to create :")
    File_Name = input()

    if os.path.exists(File_Name):
        print("File already exists")
    else:
        fobj = open(File_Name, "x")

if __name__ == "__main__":
    main()