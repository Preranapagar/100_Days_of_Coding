import requests

def is_connected():
    try:
        response = requests.get('http://www.google.com',timeout = 1)
        if response.status_code == 200:
            return True
        else:
            return False
        
    except requests.RequestException:
        return False
    
def main():

    print("Check Your Internet Connection")

    if is_connected():
        print("You are connected to internet")

    else:
        print("You are not connected to internet")

if __name__=="__main__":
    main()