import requests

def is_url_accessible(url):
    try:
        response = requests.get(url)
        # Check if the response status code indicates success (e.g., 200 OK)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

# Example usage:
url_to_check = "http://216.58.192.142"
if is_url_accessible(url_to_check):
    print(f"The URL '{url_to_check}' is accessible.")
else:
    print(f"The URL '{url_to_check}' is not accessible.")
