__author__ = 'Daniel'
from httplib2.socks import HTTPError
import urllib2
import urllib
import json
from pprint import pprint
from httplib2 import Http
from unicodedata import normalize
from datetime import datetime
import pika
from time import sleep, time

#specify hostname by name or ip adress
def establishConnection(hostname='127.0.0.1'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(hostname))
    return connection


# ,"limit":2
def importData(url, resource, limit=10000):
    data_string = urllib.quote(json.dumps({'resource_id': resource, 'limit': limit}))
    response = urllib2.urlopen(url, data_string)
    assert response.code == 200

    response_dict = json.loads(response.read())
    assert response_dict['success'] is True
    result = response_dict['result']
    # pprint(result)
    return result["records"]

lastTimeStamp = False
datetimeFormat = '%Y-%m-%dT%H:%M:%S'
programRunning = True

#msgType store, forward or transform
def wrapAndSendInitialData(inp, msgTypes, connection):
    global lastTimeStamp
    channel = connection.channel()
    channel.exchange_declare(exchange='clustertraffic', type="fanout")
    for arr in inp:
        data = {"type": msgTypes, "data": arr}
        jsonData = json.dumps(data)
        channel.basic_publish(exchange='clustertraffic', routing_key='', body=jsonData)
    lastTimeStamp = datetime.strptime(data["data"]["TIMESTAMP"], datetimeFormat)

def wrapAndSendData(inp, msgTypes, connection):
    global lastTimeStamp
    channel = connection.channel()
    # channel.exchange_declare(exchange='clustertraffic', type="fanout")
    for arr in inp:
        data = {"type": msgTypes, "data": arr}
        jsonData = json.dumps(data)
        #only publish if data is new
        currentTimeStamp = datetime.strptime(data["data"]["TIMESTAMP"], datetimeFormat)
        sentData = currentTimeStamp > lastTimeStamp
        if sentData:
            channel.basic_publish(exchange='clustertraffic', routing_key='', body=jsonData)
            lastTimeStamp = datetime.strptime(data["data"]["TIMESTAMP"], datetimeFormat)
    return sentData

def importAllData():
    connection = establishConnection()
    url = "http://ckan.projects.cavi.dk/api/action/datastore_search"
    resourceValues = "d7e6c54f-dc2a-4fae-9f2a-b036c804837d"
    # resourceMetaData = "e132d528-a8a2-4e49-b828-f8f0bb687716"
    while True:
        try:
            values = importData(url, resourceValues)
            break
        except HTTPError:
            print "Could not retrieve data, try again"
            sleep(300)
    types = ['cluster']
    print "publish initial data of size %i" % len(values)
    wrapAndSendInitialData(values, types, connection)
    #give the CKAN archive time to update data
    sleep(300)
    while programRunning:
        try:
            values = importData(url, resourceValues,500)
        except:
            continue
        time = datetime.now()
        if wrapAndSendData(values,types,connection):
            print str(time)+":published new data"
        #give the CKAN archive time to update data
        else:
            print str(time)+"new data has not been published"
        sleep(300)
    connection.close()
    return

def getMetaData(reportid):
    resource_id = "e132d528-a8a2-4e49-b828-f8f0bb687716"
    url = "http://ckan.projects.cavi.dk/api/action/datastore_search_sql?sql=select%20%22POINT_1_STREET%22," \
          "%22POINT_1_CITY%22,%22POINT_1_LAT%22,%22POINT_1_LNG%22,%22POINT_2_STREET%22,%22POINT_2_CITY%22," \
          "%22POINT_2_LAT%22,%22POINT_2_LNG%22%20from%20%22" + resource_id + "%22%20where%20%22REPORT_ID%22=" \
          + str(reportid)
    # pprint(url)
    response = urllib2.urlopen(url)
    assert response.code == 200
    response_dict = json.loads(response.read())
    # assert response_dict[u'result'] is True
    result =response_dict[u'result']
    dict = result[u"records"][0]
    meta_data = []
    for k, v in dict.iteritems():
        meta_data.append(v)
    return meta_data


def shutDown():
    global programRunning
    programRunning = False

