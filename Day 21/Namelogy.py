# Provide a Numerological value of given name, life path number and destiny number of birthdate

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
    print("You Name total :",total)

def Birth_Num(date):
    from datetime import datetime

    date = datetime.strptime(date,'%d/%m/%Y').date()
    birthday = str(date.day)

    birthnum = 0
    for i in birthday:
        birthnum += int(i)

    while birthnum >= 10:
        
    print("Your ",birthnum)    
    


def Life_path(date):
    pass



def main():
    Name = 'Prerana Pagar'#input("Enter your name :")
    Birthdate = '03/12/1995' #input("Enter your birthday in fotmat (dd/mm/yyyy):")


    Numerical(Name)
    Birth_Num(Birthdate)

if __name__=="__main__":
    main()