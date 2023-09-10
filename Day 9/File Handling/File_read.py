import os

def main():
    print("Enter the name of the file that you want to open for reading purpose:")
    File_Name = input()

    if os.path.exists(File_Name):
        fobj = open(File_Name,"r")
        if fobj:
            print("File successfully opened in read mode")
            Data = fobj.read()
            print("Data from file :", Data)


            fobj.close()
        else:
            print("Unable to open the file")
    else:
        print("There is no such files")

if __name__=="__main__":
    main()