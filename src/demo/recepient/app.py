import rpyc
import json



with open("D:\Code\HackTest\CrowdCompute_Hackathon\src\demo\\recepient\donors.json") as f:
    active_donors = json.load(f)

connObjectList = []
results = []

def connObj(obj):
    connObjectList.append(obj)


for i in active_donors:
    connObj(rpyc.connect(f"{active_donors[i]}",18861))


for i in connObjectList:
    results.append(rpyc.async_(i.root.get_answer))

k1 = results[0](8222823)
k2 = results[1](10423884)
k3 = results[2](115231122)
k4 = results[3](225231122)



while(k1.ready == False and k2.ready == False and k3.ready and k4.ready == False):
    pass


print(f" \n \n  {k1.value}, {k2.value}, {k3.value},{k4.value} \n \n ")

    


    