import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Cynd0vfRJT66ssKW7DkGvnA9MxOfuHu6nY2Yr4GoJDjy')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

delete_doc = discovery.delete_document('3da6447e-0128-40af-8dd0-3d7b738efe18', '1dc4d665-7b8d-48df-945b-fb51c2708210', 'a4c2eafc-d5c5-4173-a098-8062038d5d90').get_result()
print(json.dumps(delete_doc, indent=2))