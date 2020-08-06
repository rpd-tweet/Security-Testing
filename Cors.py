import sys
import pycurl
from io import BytesIO 

headers = {}

def get_info():
    global url
    url = input("URL : ")

def header_content(header):
    
    header = header.decode("iso-8859-1")
    if ':' in header:
        headerName, headerValue = header.split(":", 1)
        headerName = headerName.strip()
        headerValue = headerValue.strip()
       # headerName = headerName.lower()
        headers[headerName] = headerValue
    else:
        return
    
def request_CORS(url):
    try:
        curl = pycurl.Curl()
        bytes = BytesIO()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, bytes)
        curl.setopt(pycurl.SSL_VERIFYPEER, False)  
        curl.setopt(curl.HEADERFUNCTION, header_content)
        curl.perform()
        curl.close()
        print("CORS status : ")     
        if 'access-control-allow-origin' in headers.keys():
            print("Origin :",headers['access-control-allow-origin'])
        if 'access-control-allow-method' in headers.keys():
            print("Method :",headers['access-control-allow-method'])
        if 'access-control-allow-headers' in headers.keys():
            print("Headers :",headers['access-control-allow-headers'])
    except:
        print("error occured")

if __name__ == "__main__":
    
    get_info()
    request_CORS(url)
    