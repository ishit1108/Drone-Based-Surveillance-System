import pymongo
import datetime
import time
from pymongo.server_api import ServerApi

def sendImgLoop(ersgan_list,timestamp,ts,gpsNS,gpsEW):
    print('Send1')
    cluster = pymongo.MongoClient("mongodb+srv://admin:drone123@cluster0.cy9fi03.mongodb.net/?retryWrites=true&w=majority")
    print('Send2')
    db = cluster["ESRGAN_Cluster"]
    print('Send3')
    collection = db["ESRGAN_Database"]
    try:
        attribute = "ts"
        value = ts
        document = collection.find_one({attribute: value})
        print(document)
        if document == None:
            try:
                print('Send4')
                binary_data_list = []
                for x in ersgan_list:
                    with open(x, 'rb') as image_file:
                        binary_data = image_file.read()
                        binary_data_list.append(binary_data)
                print(len(binary_data_list))
                details = {'timestamp': timestamp, 'ts': ts, 'gpsNS': gpsNS, 'gpsEW': gpsEW,
                           'number': len(binary_data_list)}
                i = 0
                for x in binary_data_list:
                    details[f'img{i}'] = x
                    i += 1
                # print(details)
                result = collection.insert_one(details, bypass_document_validation=True)
                # print(result)
                # print('Hello')
            except Exception:
                pass
    except Exception:
        pass


if __name__ == '__main__':
    uri = "mongodb+srv://admin:drone123@cluster0.cy9fi03.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = pymongo.MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    sendImgLoop([],datetime.datetime.utcfromtimestamp(time.time()),"00",0,0)