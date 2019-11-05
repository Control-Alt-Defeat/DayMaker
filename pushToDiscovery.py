import os
import json
import datetime
import csv
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# DEFINING THE API KEY ASSOCIATED WITH THE BUISNESS TYPE
API_KEYS = {'restaurants': 'Cynd0vfRJT66ssKW7DkGvnA9MxOfuHu6nY2Yr4GoJDjy', 'bars': 'XXX', 'nightlife': 'XXX', 'arts & entertainment': 'XXX'}

# DEFINING THE ENVIRONMENT ID ASSOCIATED WITH THE BUISNESS TYPE
ENVIRONMENT_IDS = {'restaurants': '3da6447e-0128-40af-8dd0-3d7b738efe18', 'bars': 'XXX', 'nightlife': 'XXX', 'arts & entertainment': 'XXX'}

# DEFINING THE COLLECTION ID ASSOCIATED WITH THE BUISNESS TYPE
COLLECTION_IDS = {'restaurants': '1dc4d665-7b8d-48df-945b-fb51c2708210', 'bars': 'XXX', 'nightlife': 'XXX', 'arts & entertainment': 'XXX'}

def upload_to_discovery(filename, alias, buisness_type):  
    # LOAD MASTERDOCINFO TO BE READ
    aliasfile = open('docAliases.txt', 'r+')
    aliaslist = aliasfile.read().split('\n')

    if alias not in aliaslist:
        # APPEND THE NEW ALIAS AND CLOSE THE DOCALIASFILE
        aliasfile.write(alias + "\n")
        aliasfile.close()

        # AUTHENTICATING AND CONNECTING TO WATSON DISCOVERY
        authenticator = IAMAuthenticator(API_KEYS[buisness_type])
        discovery = DiscoveryV1(
            version='2019-04-30',
            authenticator=authenticator
        )

        discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

        # DECLARING WHAT ENVIRONMENT AND COLLECTION THE FILE SHOULD BE ADDED TO
        environment_id = ENVIRONMENT_IDS[buisness_type]
        collection_id = COLLECTION_IDS[buisness_type]

        # ADDING THE PROVIDED DOCUMENT TO DISCOVERY
        with open(os.path.join(os.getcwd(), filename)) as fileinfo:
            add_doc = discovery.add_document(environment_id, collection_id, file=fileinfo, file_content_type='application/json').get_result()
        document_id = add_doc["document_id"]

        # CLOSE THE DISCOVERY FILE STREAM
        fileinfo.close()

        # UPDATE A LIST FOR MASTERDOCINFO WITH ALL RELEVANT INFORMATION
        docinfo = [buisness_type, alias, environment_id, collection_id, document_id, datetime.datetime.today().strftime("%m/%d/%y")]

        # LOAD MASTERDOCINFO TO BE READ AND PTENTIALY APPENDED TO
        with open(os.path.join(os.getcwd(), 'masterDocInfo.csv'), 'a') as csvfile:
            writeCSV = csv.writer(csvfile, lineterminator='\n')

            # WRITE THE NEW RESULTS TO MASTERDOCINFO
            writeCSV.writerow(docinfo)

        # CLOSE THE MASTERDOCINFO FILE STREAM
        csvfile.close() 