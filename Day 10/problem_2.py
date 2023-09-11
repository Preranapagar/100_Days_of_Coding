#write a program which accept file name from user and open that file and display the contents of that file on screen
import os

def main():
    File_name = input("Enter the file name :")

    if os.path.exists(File_name):
        fobj = open(File_name,'r')
        print(f"{File_name} opened.....")
        
        for line in fobj:
            print(line)
        
        fobj.close()

    else:
        print("File dosen't exist")

if __name__ == "__main__":
    main()
