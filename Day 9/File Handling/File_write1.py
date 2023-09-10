import os

def main():
    print("Enter the name of the file that you want to open for writing purpose:")
    File_Name = input()

    if os.path.exists(File_Name):
        fobj = open(File_Name,"w") #write mode
        if fobj:
            print("File successfully open in writing mode ")

            print("Enter your data :")
            Data = input()
            fobj.write(Data) #write the data into file

            fobj.close()
        else:
            print("Unable to open the file")
    else:
        print("There is no such files")

if __name__=="__main__":
    main()