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
    print(total)



def main():

    # Name = input("Enter your name :")
    n = 'Prerana Pagar'

    Numerical(n)

if __name__=="__main__":
    main()