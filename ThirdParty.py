# Scan all third party URLs and check sensitive informations in URL.

import requests
import json
from urllib.parse import urlparse 
from urllib.parse import parse_qs

# get url, data from user
def get_info():
    global url, username, domain, password, data, method
    url = input("URL : ")
    domain = input("Domain : ")

def  check_third_party():
    parsed_data = urlparse(url)
    if parsed_data.hostname == domain:
        return False
    return True


def check_for_sensitive_info():
    try:
        response = requests.get(url)
        parsed_data = urlparse(url)
        scheme = parsed_data.scheme
        host = parsed_data.hostname
        query = parse_qs(parsed_data.query)
        fragment = parsed_data.fragment
        print("\nSensitive Informations in {} :".format(url))
        if scheme: print("Schema :", scheme) 
        if host: print("Host :", host)
        if query: print("Query :", query)
        if fragment: print("Fragment :", fragment)
        
    except:
        print("error occured")


def check_for_sensitive_info_util():
    if check_third_party():
        print("Third party")
    else:
        print("Not a third party")
    check_for_sensitive_info()
    


if __name__ == "__main__":
    
    get_info()
    check_for_sensitive_info_util()
    