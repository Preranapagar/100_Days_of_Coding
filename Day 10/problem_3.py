#write a program which accepts file name from user and create new file named as demo.txt and copy all contains
#from existing file into new file. accept the file name through command line aurgument
import os
import sys

def main():
    argv = sys.argv
    
    if len(argv)==1:
        print("You did not enter file name in command line prompt")
    else:
    
        file_name = sys.argv[1]

            
        if os.path.exists(file_name):
            print(f"opening {file_name} to copy content")

            fobj = open(file_name,'r')
            data = fobj.read()

            new_file = input("Enter the name of new file :")
            fobj2 = open(new_file,'w')
            fobj2.write(data)

            print("Your content is copied.....")

            fobj.close()
            fobj2.close()

        else:
            print(f"{file_name} dosen't exist in your directory.")
            

if __name__ == "__main__":
    main()

