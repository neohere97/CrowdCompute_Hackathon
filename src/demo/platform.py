from flask import Flask,request
import json


donors = dict()
app = Flask(__name__)
@app.route('/donorAttach', methods=['POST'])
def index():
    data = json.loads(request.data.decode("utf-8"))
    
    if data["HostName"] in donors:
        pass
    else:        
        donors[data["HostName"]] = data["HostIP"]    
    
    return 'OK',200
@app.route('/getClients',methods=['POST'])
def ret():
    return donors
    
if __name__ == '__main__':
    app.run(debug=True)
