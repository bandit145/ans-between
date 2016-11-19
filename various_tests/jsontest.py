import requests
import json
#jsonthing = json.dumps({'wat':'idk'})
#print(str(jsonthing))
#print(json.loads(jsonthing))t
req = requests.post('http://localhost:8080/job', data=json.dumps({'name':'server_deploy', 'params':[{'-i':'hosts'},{'--extra-vars':'vars'},{'--private-key':'pkey'}], 'args':['--ask-become-pass'],'password':'password','auth':'123456'}), headers={'content-type':'application/json'})
print(req.content)

req = requests.post('http://localhost:8080/job',data=json.dumps({'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2'],'password':'123456','auth':'123456'}),headers={'content-type':'application/json'})
print(req.content)
#{'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2'],'password':'123456','auth':'123456'}
#{'name':'test1','params':[{'-i':'192.168.1.8'}],'args':['arg1','arg2'],'password':'123456','auth':'123456'}
# curl -X POST -H "Content-Type":"application/json" -d '{"name":"server_deploy.yml", "params":[{"-i":"192.168.1.34,"},{"--extra-vars":"host_name=meme-test"},{"--private-key":"pkey"}], "args":["--ask-become-pass"],"password":"test","auth":"123456"}' http://192.168.1.33:8080/job
