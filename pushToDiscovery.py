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

def upload_to_discovery(filename):  
    # ERROR HANDLING
    try:
        # DECLARING WHAT ENVIRONMENT AND COLLECTION THE FILE SHOULD BE ADDED TO
        environment_id = '3da6447e-0128-40af-8dd0-3d7b738efe18'
        collection_id = '1dc4d665-7b8d-48df-945b-fb51c2708210'

        # ADDING THE PROVIDED DOCUMENT
        with open(os.path.join(os.getcwd(), filename)) as fileinfo:
            add_doc = discovery.add_document(environment_id, collection_id, file=fileinfo, file_content_type='application/json').get_result()
        print(json.dumps(add_doc, indent=4))

        # CLOSE THE FILE STREAM
        fileinfo.close()
        
        # UPDATE THE DATABASE WITH THE DOCUMENT ID AND OTHER RELEVANT INFORMATION

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)