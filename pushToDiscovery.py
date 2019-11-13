import config
import os
import json
import datetime
import csv
import time
from ibm_watson import DiscoveryV1
<<<<<<< HEAD
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# DEFINING THE API KEY ASSOCIATED WITH THE BUISNESS TYPE
API_KEYS = {'restaurants': 'Cynd0vfRJT66ssKW7DkGvnA9MxOfuHu6nY2Yr4GoJDjy', 'bars': '2YpsPbSxOZs4XODvqwtn-LhDRZFtzVjFapFR93BjrDHy', 'arts & entertainment': 'tbjy8l9-78zto0HHD3PgeZflH4wGdbzXM-1HgHbGkWii'}

# DEFINING THE ENVIRONMENT ID ASSOCIATED WITH THE BUISNESS TYPE
ENVIRONMENT_IDS = {'restaurants': '3da6447e-0128-40af-8dd0-3d7b738efe18', 'bars': '139f7aba-2a1f-4476-b9c8-38de592a1e00', 'arts & entertainment': 'e5856d24-400e-4691-a898-e0e07b6bccbf'}

# DEFINING THE COLLECTION ID ASSOCIATED WITH THE BUISNESS TYPE
COLLECTION_IDS = {'restaurants': '19e88269-e9a7-4d24-adcb-e9ea32638b55', 'bars': '2a87b3fa-94ae-4680-ac88-40ec1e80ca82', 'arts & entertainment': '6a2d3bef-8b4e-482e-866b-1091ad110d5d'}

# DEFINING THE URL ASSOCIATED WITH THE BUISNESS TYPE
DIS_URL = {'restaurants': 'https://gateway.watsonplatform.net/discovery/api', 'bars': 'https://gateway-wdc.watsonplatform.net/discovery/api', 'arts & entertainment': 'https://gateway.watsonplatform.net/discovery/api'}

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

        discovery.set_service_url(DIS_URL[buisness_type])

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
=======
from ibm_watson import ApiException

# discovery = DiscoveryV1(
#     version='2019-04-30',
#     iam_apikey='Cynd0vfRJT66ssKW7DkGvnA9MxOfuHu6nY2Yr4GoJDjy',
#     url='https://gateway.watsonplatform.net/discovery/api'
# )

# ENTERING AUTHENTICATION AND REQUIREMENTS FOR WATSON DISCOVERY
# discovery.set_url('https://gateway-wdc.watsonplatform.net/discovery/api')
# discovery.set_iam_apikey('Cynd0vfRJT66ssKW7DkGvnA9MxOfuHu6nY2Yr4GoJDjy')

# ERROR HANDLING
try:
    # DECLARING WHICH FILE TO SEND AND TO WHAT ENVIRONMENT AND COLLECTION IT SHOULD BE ADDED TO
    path_element = 'dataPull.py'
    filename = 'yelpResponse.json'
    config.environment_id = '3da6447e-0128-40af-8dd0-3d7b738efe18'
    config.collection_id = '1dc4d665-7b8d-48df-945b-fb51c2708210'

    # ADDING A DOCUMENT
    with open(os.path.join(os.getcwd(), filename)) as fileinfo:
        add_doc = config.discovery.add_document(config.environment_id, config.collection_id, file=fileinfo, file_content_type='application/json').get_result()
    print(json.dumps(add_doc, indent=4))

except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)
>>>>>>> 6f35daca2cd69c23eb7e581d3188099dc7522977
