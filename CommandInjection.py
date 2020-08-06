# command injection

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
        
# check for injection in login data
def check_spl_char():
    spl_char = ['\'', '=', " ", "&", '"', "#", "%20", "%09", "$IFS&9", "%0b", "0a", "%0d", ";", "&", "|", "%1a", "}", "{", "%25", "%00", "%F0%9F%92%A9", "%20#", "%20::"]
    for i in spl_char:
        for j in data.values():
            if i in j:
                return False
    return True
       
   

def request_login():
    try:
        if check_spl_char():    
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
        
