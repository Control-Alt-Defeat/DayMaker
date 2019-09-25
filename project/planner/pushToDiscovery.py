import config
import os
import json
from ibm_watson import DiscoveryV1
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