import os

def main():
    File_Name = input("Enter the name of file:")

    if os.path.exists(File_Name):
        os.remove(File_Name)
    else:
        print("No such file exists")

if __name__=="__main__":
    main()


