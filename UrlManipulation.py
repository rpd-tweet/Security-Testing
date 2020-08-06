# URL Manipulation (request parameters and URL path)

import requests
from urllib.parse import urljoin
import json



def get_info():
    global url, manipulated_string, username, password, data, method
    url = input("URL : ")
    manipulated_string = input("Manipulated String : ")
    method = input("Request method (GET, POST): ").lower()
    if method == "get" :
        print("Incase of Authentication enter username and password else skip:")
        username = input("Username : ")
        password = input("Password : ")
        data = json.loads(input("Data (as dict) : "))
    else:
        data = json.loads(input("Data (as dict) : "))
        
      

def check_for_url_manipulation():
    try:
        manipulated_url = urljoin(url, manipulated_string)
        print(manipulated_url)
        session = requests.Session()
        # request method from user
        if method == "get" :
            response = session.get(manipulated_url, auth = (username, password), data = data)
        if method == "post" :
            response = session.post(manipulated_url, data = data) 
        if response.status_code != 404:
            print("URL Manipulation attack successful")
        else:
            print("URL cannot be manipulated")
    except:
        print("error occured")

 

if __name__ == "__main__":
    get_info()
    check_for_url_manipulation()