# Sensitive Information in URL

import requests
import sys
import json


def get_info():
    global url, username, password, data, method
    url = input("URL : ")
    method = input("Request method (GET, POST): ").lower()
    if method == "get" :
        print("Incase of Authentication enter username and password else skip:")
        username = input("Username : ")
        password = input("Password : ")
        data = json.loads(input("Data (as dict) : "))
    else:
        data = json.loads(input("Data (as dict) : "))
        
        
def check_for_server_info():
    try:
    
        session = requests.Session()
        # request method from user
        if method == "get" :
            response = session.get(url, auth = (username, password), data = data)
        if method == "post" :
            response = session.post(url, data = data)  
        headers = {}
        print("Server Info : ")         
        serverInfo = ["X-Powered-By", "Server"]     #
        for i in serverInfo:
            if i in response.headers:
                headers[i] = response.headers[i]
        jsonData = json.dumps(headers, indent = 4)   
        if len(jsonData) > 0:
            print(jsonData)
        else:
            print("None Found")
    except:
        print("error occured")
       
    


if __name__ == "__main__":
    
    get_info()
    check_for_server_info()