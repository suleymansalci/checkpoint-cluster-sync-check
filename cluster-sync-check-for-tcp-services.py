import json
import requests

login = requests.post('https://cplab:4434/web_api/v1.5/login', json={'user': 'admin', 'password': 'pass1234'}, verify=False)


print("\n-----------------SID'i buldum-------------------------: ",login.json()["sid"] + "\n")

response = requests.post('https://cplab:4434/web_api/v1.5/show-services-tcp', json={'details-level' : 'full', 'limit' : 500,}, headers={'X-chkp-sid': login.json()["sid"]}, verify=False)



for p in (range(len(response.json()["objects"]))):
    if response.json()["objects"][p]["sync-connections-on-cluster"] == False:
        print ("Cluster sync is disabled: ", response.json()["objects"][p]["name"])