#create a class School and Display student Info
class School:
    SchoolName = "R.K.M. English School"
    
    def __init__(self,Name,Std,Div):
        self.StudentName = Name
        self.Standard = Std
        self.Division = Div

    def StudentInfo(self):
        print("Name of Student :", self.StudentName)
        print("Standard of Student :", self.Standard)
        print("Division of Student :", self.Division)


def main():

    print("School Name :", School.SchoolName)

    Student1 = School("Aakash", 7, "D")

    Student1.StudentInfo()

if __name__=="__main__":
    main()