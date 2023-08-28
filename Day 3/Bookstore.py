
'''write a program which contains one class named BookStore. BookStore class contains two instance varibales as Name, Author.
 That Class contains one class variable as NoOfBooks which is initialise to 0. There is one instance methods of class as Display 
 which Displays name, author and number of books. initialise instance variable in init method by accepting values from user as name and author.
 Inside init method increment value of NoOfBooks by 1.'''

class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.BookName = Name
        self.Author = Author
        BookStore.NoOfBooks +=1

    def Display(self):
        print("Name of Book :", self.BookName)
        print("Name of Author :", self.Author) 
        print("Number of Books :", BookStore.NoOfBooks)

def main():
    
    Obj1 = BookStore("Power of Positive Thinking","Norman Vincent Peale")
    Obj1.Display()

    Obj2 = BookStore("Powe of Your Subconcious Mind","Dr.Joseph Murphy")
    Obj2.Display()

    Obj3 = BookStore("Milk and Honey","Rupi Kaur")
    Obj3.Display()

if __name__=="__main__":
    main()

 