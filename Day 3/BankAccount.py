"""write a program which contains one class name as BankAccount. Class contains two instance variables as Name and Amount.
class has one class varaible ROI which is initialise to 10.5. inside init method initialise all Name and Amount method by accepting 
values from user. There are four instance methods inside class as Display(), Deposit(), Withdraw(), and CalculateIntrest()."""

class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name

        if type(Amount) is int or type(Amount) is float :
            self.Amount = Amount
            print("Welcome "+self.Name)
            print("Your account is created with balance Rs. ",self.Amount)
            print()
        else:
            print(f"Dear, {self.Name} you have entered wrong information")
            print()

    def Display(self):
        print("Name of account holder :", self.Name)
        print("Your account balance is :", self.Amount)
        print()


    def Deposit(self,Value):
        self.Amount = self.Amount + Value
        print(f"Amount deposited to {self.Name}'s account...:", Value)
        print(f"{self.Name} your current account balance is :", self.Amount)
        print()

    def Withdraw(self,Value):
        if (self.Amount > Value):
            self.Amount =self.Amount - Value
            print(f"Amount withdrawn from {self.Name}'s account...:", Value)
            print(f"{self.Name} your account balance is :", self.Amount)
            print()
        else:
            print(f"Dear, {self.Name} you don't have sufficient balance ")
            print()
        
    def CalculateIntrest(self):
        Intrest = (self.ROI/100)*self.Amount
        print(f"{self.Name} your account balance is :", self.Amount)
        print(f"Intrest on {self.Name}'s account is :", Intrest)
        print()

def main():

    Name = input("Enter the user Name :")
    Balance = int(input("Enter the amount to create account :"))

    Obj = BankAccount(Name, Balance)

    print("Select below to perform operation on your Account")
    print("""
1 . To Check Account Balance
2 . To Deposit Amount
3 . To Withdraw Amount
4 . To Calculate Intrest""")
    print()
    
    op = int(input("Enter :"))

    if op == 1:
        Obj.Display()
    elif op == 2:
        Obj.Deposit(int(input("Amount:")))
    elif op == 3:
        Obj.Withdraw(int(input("Amountt:")))
    elif op == 4:
        Obj.CalculateIntrest()


if __name__=="__main__":
    main()