from flask import Flask,request
import json
import httplib2


donors = dict()
recepient = dict()

app = Flask(__name__)
@app.route('/donorAttach', methods=['POST'])
def donorAttach():
    data = json.loads(request.data.decode("utf-8"))
    
    if data["HostName"] in donors:
        pass
    else:        
        donors[data["HostName"]] = data["HostIP"]
        dump_to_json("donor")    
        
    return 'OK',200

@app.route('/recepientAttach', methods=['POST'])
def recepientAttach():
    data = json.loads(request.data.decode("utf-8"))
    
    if data["HostName"] in recepient:
        pass
    else:        
        recepient[data["HostName"]] = data["HostIP"]
        dump_to_json("recepient")    
        
    return 'OK',200

@app.route('/getClients',methods=['POST'])
def ret():
    with open("src/demo/platform/active_hosts.json") as f:
        active_hosts = json.load(f)
    
    return json.dumps(active_hosts)

    

def dump_to_json(val):
    if(val == "donor"):
        with open('src/demo/platform/active_hosts.json','w') as outfile:
            json.dump(donors,outfile)
    else:
        with open('src/demo/platform/active_recp.json','w') as oufile:
            json.dump(recepient,oufile)
    
if __name__ == '__main__':
    app.run(debug=True)
