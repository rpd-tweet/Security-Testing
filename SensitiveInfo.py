# Sensitive Information in URL
import requests
import json
from urllib.parse import urlparse 
from urllib.parse import parse_qs

# get url, data from user
def get_info():
    global url, username, domain, password, data, method
    url = input("URL : ")


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


if __name__ == "__main__":
    
    get_info()
    check_for_sensitive_info()
    