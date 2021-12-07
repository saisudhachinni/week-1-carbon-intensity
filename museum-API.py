import json
import pprint

import requests

values_append=[]
response=requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects')
response1=requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/5')

#int(response.content,'hello')
#print(type(response1.json()))#dict
#print(type(response1.content))#bytes

v=response.json()#dict
#print(json.dumps(v, indent=5))
for i,j in v.items():
    if i =='objectIDs':
        for k in j:
            values_append.append(k)
    #for k in j:
    #    print(k,'kkkkkk')
#print(values_append)
for list_items in values_append:
    print(list_items)
    response1 = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(list_items))


