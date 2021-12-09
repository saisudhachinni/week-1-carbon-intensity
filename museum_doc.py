import json

import requests

headers = {
    'Accept': 'application/json'
}


url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'      # basic url from the carbon intensity

def get_objectid(headers,url):
    """
    this function is used to get the reaponse from headers url
    to get the response from json
    :param headers:
    :param url: parameters from basic url
    :return: to return the statement file name
    """
    response=requests.get(url,headers=headers)
    json_data=response.json()
    if response.ok==True:
        data = response.content
        with open('data.json', 'wb') as f:
            f.write(data)
    #print(f.name)
    return f.name

json_object_file=get_objectid(headers,url)
#json_object_file#data.json



def read_object_columns(json_object_file):
    """
    to write the function from json object file
    :param json_object_file:
    :return: to return the statement from object id
    """
    json_object_file
    with open(json_object_file) as json_data:
        d=json.load(json_data)
    objectid=d['objectIDs']
    return objectid #list
objectid=read_object_columns(json_object_file)


def calling_api(objectid):
    """
    this function writting to call the objectid
    have to take the basic url
    to print the statement with response
    :param objectid:
    :return:
    """
    count=0
    for i in objectid:
        if count>=10:
            break
        url='https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(i)
        response_individual=requests.get(url)
        print(response_individual.json())
        count = count + 1

 # calling_api(objectid)


