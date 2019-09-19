"""
    Example call:
        ./examples.py "[API Key]"

    For additional reference look here https://github.com/gfairchild/yelpapi and more specifically example.py
"""

from yelpapi import YelpAPI
import argparse
from pprint import pprint

import json

argparser = argparse.ArgumentParser(description='Example Yelp queries using yelpapi. Visit https://www.yelp.com/developers/v3/manage_app to get the necessary API keys.')
argparser.add_argument('api_key', type=str, help='Yelp Fusion API Key')
args = argparser.parse_args()

yelp_api = YelpAPI(args.api_key)


# SEARCH BY LOCATION TEXT AND TERM
response = yelp_api.search_query(location='columbus, oh', sort_by='rating', limit=5)
    
# WRITE THE RESULTS OF THE API CALL TO A NEW FILE
f = open("yelpResponse.json", "w")
filteredResponse = json.dumps(response, indent=4)
f.write(filteredResponse)

# WRITE THE RESULTS OF THE API CALL TO A NEW FILE WHERE EACH BUISNESS WILL HAVE THEIR OWN FILE
i = 0
while i < len(response["businesses"]):
    f = open("yelpResponse" + str(i) + ".json", "w")
    filteredResponse = json.dumps(response["businesses"][i], indent=4)
    f.write(filteredResponse)
    i += 1