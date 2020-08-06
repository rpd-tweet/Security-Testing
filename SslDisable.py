#ssl testing


import pycurl
from io import BytesIO 


def get_info():
    global url
    url = input("URL : ")

        
    
def ssl_disable():
    try:
        curl = pycurl.Curl()
        bytes = BytesIO()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, bytes)
        curl.setopt(pycurl.SSL_VERIFYPEER, False)       
        curl.perform()
        curl.close()
        print("SSL disabled")
        
    except:
        print("error occured")

if __name__ == "__main__":
    
    get_info()
    ssl_disable()