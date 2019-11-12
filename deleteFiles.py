import json
import argparse
import os
import pandas as pd
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# PARSE FOR USER INPUT AND VALIDATE IT
argparser = argparse.ArgumentParser(description='Deletes a certain type of buisness to IBM\'s Discovery database')
argparser.add_argument('buisness_type', type=str, choices = ['restaurants', 'bars', 'nightlife', 'arts & entertainment'], help='Valid buisness type (restaurants, bars, nightlife, or arts & entertainment)')
argparser.add_argument('deletion_file', type=str, choices = ['restaurants_delete.txt', 'bars_delete.txt', 'nightlife_delete.txt', 'arts_entertainment_delete.txt'], help='Valid .txt file with a list of aliases to be deleted')
args = argparser.parse_args()

# DEFINING THE API KEY ASSOCIATED WITH THE BUISNESS TYPE
API_KEYS = {'restaurants': 'Cynd0vfRJT66ssKW7DkGvnA9MxOfuHu6nY2Yr4GoJDjy', 'bars': '2YpsPbSxOZs4XODvqwtn-LhDRZFtzVjFapFR93BjrDHy', 'nightlife': 'XXX', 'arts & entertainment': 'XXX'}

# DEFINING THE URL ASSOCIATED WITH THE BUISNESS TYPE
DIS_URL = {'restaurants': 'https://gateway.watsonplatform.net/discovery/api', 'bars': 'https://gateway-wdc.watsonplatform.net/discovery/api', 'nightlife': 'XXX', 'arts & entertainment': 'XXX'}

# AUTHENTICATING AND CONNECTING TO WATSON DISCOVERY
authenticator = IAMAuthenticator(API_KEYS[args.buisness_type])
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

discovery.set_service_url(DIS_URL[args.buisness_type])

# OPEN UP THE FILE OF DOCUMENTS TO DELETE
with open(os.path.join(os.getcwd(), args.deletion_file)) as deletioninfo:
    alias_names = [line.strip() for line in deletioninfo]

    # ITERATE THROUGH THE TEXT FILE OF ALIASES TO DELETE
    for alias in alias_names

        # PULL OUT ALL THE NECESSARY INFO FROM THE MASTERDOCINFO


        # DELETE THE FILE 
        delete_doc = discovery.delete_document('3da6447e-0128-40af-8dd0-3d7b738efe18', '1dc4d665-7b8d-48df-945b-fb51c2708210', 'a4c2eafc-d5c5-4173-a098-8062038d5d90').get_result()