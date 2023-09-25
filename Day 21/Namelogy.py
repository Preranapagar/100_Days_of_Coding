# Provide a Numerological value of given name, life path number and destiny number of birthdate
def digit_sum(num):
    while num >= 10:
        sum_digit = 0
        while num > 0:
            sum_digit += num % 10
            num //= 10

        num = sum_digit

    return num

def Numerical(string):
    print("_______________________________Your Numeroloy Report_______________________________")

    value_dict = {1:['a','j','s'], 2:['b','k','t'], 3:['c','l','u'], 4:['d','m','v'], 5:['e','n','w'],
                  6:['f','o','x'], 7:['g','p','y'], 8:['h','q','z'], 9:['r','i']}
    string = string.lower()

    key_val = []

    for char in string:
        for key, value_list in value_dict.items():
            if char in value_list:
                key_val.append(key)

    total = sum(key_val)
    total = digit_sum(total)

    print("You Name total :",total)

def Birth_Num(date):
    from datetime import datetime

    date = datetime.strptime(date,'%d/%m/%Y').date()
    birthday = int(date.day)
    birthday = digit_sum(birthday)

    print("Your Birth Number is :", birthday)


def Life_path(date):
    digit = 0

    for i in date:
        if i.isdigit():
            digit += int(i)

    digit = digit_sum(digit)
    
    print("Your Life Path Number is :", digit)

def main():
    Name = input("Enter your name :")
    Birthdate = input("Enter your birthday in format (dd/mm/yyyy):")


    Numerical(Name)
    Birth_Num(Birthdate)
    Life_path(Birthdate)

if __name__=="__main__":
    main()