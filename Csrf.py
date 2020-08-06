# Check CSFR token used for form/post request

import requests
import re
import json

# get url, data from user
def get_info():
    global url, username, password, data, method
    url = input("URL : ")
    method = input("Request method (GET, POST): ").lower()
    if method == "get" :
        print("Incase of Authentication enter username and password else skip:\n")
        username = input("Username : ")
        password = input("Password : ")
        data = json.loads(input("Data (as dict) : "))
    else:
        data = json.loads(input("Data (as dict) : "))
    


def request():
    try:
        session = requests.Session()
        try:
            session.get(url)
            data["csrfmiddlewaretoken"] = session.cookies["csrftoken"]
        except:
            pass
        # request method from user
        if method == "get" :
            response = session.get(url, auth = (username, password), data = data)
        if method == "post" :
            session.post(url, data = data)   
            response = session.get(url)
        status_code = response.status_code
        if status_code == 200:
            print("Request made successfully")
        else:
            print("Unsuccessful request")
        
    except:
        print("Error")


     
if __name__=="__main__":

    get_info()
    request()
        
