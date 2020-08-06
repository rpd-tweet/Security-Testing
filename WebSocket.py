# Test a WebSocket using curl.


import pycurl
from io import BytesIO 

headers = {}

def get_info():
    global url
    url = input("URL : ")

        

def header_content(header):
    
    header = header.decode("iso-8859-1")
    if ':' in header:
        header_name, header_value = header.split(":", 1)
        header_name = header_name.strip()
        header_value = header_value.strip()
        headers[header_name] = header_value
    else:
        return
    
def check_for_connection():
    try:
        curl = pycurl.Curl()
        bytes = BytesIO()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, bytes)
        curl.setopt(curl.SSL_VERIFYPEER, False)
        curl.setopt(curl.HEADERFUNCTION, header_content)
        curl.perform()
        curl.close()
        try:
            if headers["Connection"]:
                print("Not a web socket connection")
        except:
            print("Web socket connection closed")
    except:
        print("error occured")
      


if __name__ == "__main__":
    
    get_info()
    check_for_connection()
    