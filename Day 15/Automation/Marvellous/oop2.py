class Demo:

    def __init__(self,Value1,Value2): #constructor
        print("Inside init method")
        self.No1 = Value1
        self.No2 = Value2

    def Display(self):
        print("Value of No1:", self.No1)
        print("Value of No2:",self.No2)



def main():
    print("Demonstartion of Object Orientation")

    Obj1 = Demo(10,20) #__init__(100,10,20)
    Obj2 = Demo(11,22) #__init__(200,11,22)

    Obj1.Display()
    Obj2.Display()

if __name__=="__main__":
    main()