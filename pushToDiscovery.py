import os
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Cynd0vfRJT66ssKW7DkGvnA9MxOfuHu6nY2Yr4GoJDjy')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

# DEFINING THE ENVIRONMENT ID ASSOCIATED WITH THE BUISNESS TYPE
ENVIRONMENT_IDS = {'resturants': '3da6447e-0128-40af-8dd0-3d7b738efe18', 'bars': 'XXX', 'nightlife': 'XXX', 'arts & entertainment': 'XXX'}

# DEFINING THE COLLECTION ID ASSOCIATED WITH THE BUISNESS TYPE
COLLECTION_IDS = {'resturants': '1dc4d665-7b8d-48df-945b-fb51c2708210', 'bars': 'XXX', 'nightlife': 'XXX', 'arts & entertainment': 'XXX'}

def upload_to_discovery(filename, buisness_type):  
    # ERROR HANDLING
    try:
        # DECLARING WHAT ENVIRONMENT AND COLLECTION THE FILE SHOULD BE ADDED TO
        environment_id = ENVIRONMENT_IDS[buisness_type]
        collection_id = COLLECTION_IDS[buisness_type]

        # ADDING THE PROVIDED DOCUMENT
        with open(os.path.join(os.getcwd(), filename)) as fileinfo:
            add_doc = discovery.add_document(environment_id, collection_id, file=fileinfo, file_content_type='application/json').get_result()
        print(json.dumps(add_doc, indent=4))

        # CLOSE THE FILE STREAM
        fileinfo.close()
        
        # UPDATE THE MASTER_ WITH THE DOCUMENT ID AND OTHER RELEVANT INFORMATION

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)