#  SQL injection test on search keyword and request parameters

import requests
import sys
import urllib.parse
import json

def get_info():
    global url, username, password, data, method
    url = input("URL : ")
    url = urllib.parse.unquote(url)
    method = input("Request method (GET, POST): ").lower()
    if method == "get" :
        print("Incase of Authentication enter username and password else skip:")
        username = input("Username : ")
        password = input("Password : ")
        data = json.loads(input("Data (as dict) : "))
    else:
        data = json.loads(input("Data (as dict) : "))
        
        

def check_spl_char(): 
    spl_char = ['\'', '=', '"', "#"]
    for i in spl_char:
        if i in username:
            return False
        if i in password:
            return False
        for j in data.values():
            if i in j:
                return False
    return True
   
   
    # request for login  using csrftoken 
def request_login():
    try:
        if  check_spl_char():    
            session = requests.Session()
        # request method from user
            if method == "get" :
                response = session.get(url, auth = (username, password), data = data)
            if method == "post" :
                response = session.post(url, data = data) 
            print("Valid request made")  
        else:
            print("Invalid characters in login data")
    except:
        print("error occured")
     
     
if __name__=="__main__":
    
    get_info()
    request_login()
        
              



