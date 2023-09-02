from datetime import datetime

def main():
    
    print("Current Time :", datetime.now())
    print("Today's Datetime :", datetime.today())

    Today = datetime.today()

    print("Today's date:", Today.date())
    print("Today' day :", Today.day)
    print("Today's weekday :", Today.weekday())

    print("Type :", type(Today))

    Today_1 = datetime.strftime(Today,'%d-%m-%Y')
    print(type(Today_1))

    print("Current Month :", Today.strftime("%B"))



if __name__=="__main__":
    main()