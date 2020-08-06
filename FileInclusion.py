# vulnerability allows an attacker to include a file on the web server.
import requests
import json
import re
import urllib.parse

# get url, data from user
def get_info():
    global url, username, password, data, method
    url = input("URL : ")
    url = urllib.parse.unquote(url)
    method = input("Request method (GET, POST): ").lower()
    if method == "get" :
        print("Incase of Authentication enter username and password else skip:\n")
        username = input("Username : ")
        password = input("Password : ")
        data = json.loads(input("Data (as dict) : "))
    else:
        data = json.loads(input("Data (as dict) : "))
 
def validate_data():
    if re.findall('=http|:\\\\|../../../|%00\Z', url) :
        return False
    for value in data.values() : 
        print(value)
        key_match = re.findall('=http|:\\\\|../../../|%00\Z', value)  
        if key_match:
            return False
    return True
          
    
def check_for_script():
    try:
        if validate_data() :
            session = requests.Session()
            # request method from user
            if method == "get" :
                response = session.get(url, auth = (username, password), data = data)
            if method == "post" :
                response = session.post(url, data = data)  
            if response.status_code == 200 :
                print("Request made,No vulnerability found")
            else:
                print("Request unsuccessful, No vulnerability found")
        else:
            print("Inclusion found")
    except:
        print("error occured")

     
if __name__=="__main__":
    
    get_info()
    check_for_script()

        