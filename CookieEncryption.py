# Check the cookies to verify encryption on sensitive information.

import requests
import re
import json

# get url, data from user
def get_info():
    global url, username, password, data, method
    url = input("URL : ")
    method = input("Request method (GET, POST): ").lower()
    if method == "get" :
        username = input("Username : ")
        password = input("Password : ")
        data = json.loads(input("Data (as dict) : "))
    else:
        data = json.loads(input("Data (as dict) : "))



    # check for cookie encryption
def check_encryption():
    try:
        search_key = "Secure"
        session = requests.Session()
        # request method from user
        if method == "get" :
            response = session.get(url, auth = (username, password), data = data)
        if method == "post" :
            response = session.post(url, data = data)  
        response_headers = response.headers
        try:
            cookies = response_headers["Set-Cookie"]
            
            # Checks if header has secure and HttpOnly flag
            if search_key in cookies and "HttpOnly" in cookies:
                print("\nCookies encrypted")
            else:
                print("\nInsecure cookies")
        except:
            print("No cookies Found")
    except:
        print("Error")


     
if __name__=="__main__":

    get_info()
    check_encryption()
        
