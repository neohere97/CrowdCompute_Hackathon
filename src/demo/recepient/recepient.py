import httplib2
import json
import time
import datetime
import socket
from subprocess import call

def dump_to_json(val):
    with open('recepient/donors.json','w') as outfile:
        json.dump(val,outfile)

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

    url_recepientAttach = "http://127.0.0.1:5000/recepientAttach"
    url_getClients = "http://127.0.0.1:5000/getClients"
    
    data = {    'HostName': host_name,
                'HostIP':   host_ip
                
           }

    headers = {'Content-Type': content_type_header}   

    while True:
        response, content = http.request( url_recepientAttach,
                                          'POST',
                                          json.dumps(data),
                                          headers=headers)
        if(response["status"] == "200"):
            response, content = http.request( url_getClients,
                                          'POST',
                                          json.dumps(data),
                                          headers=headers)
            
            dump_to_json(json.loads(content.decode("utf-8")))
            break
                        

    call(["python","recepient/app.py"])
            

            
        
        

