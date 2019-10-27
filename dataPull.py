"""
    Example call:
        ./examples.py "[API Key]"

    For additional reference look here https://github.com/gfairchild/yelpapi and more specifically example.py
"""

from yelpapi import YelpAPI
import argparse
from pprint import pprint

import json
import os
import pushToDiscovery

yelp_api = YelpAPI("fsx7o9fQIvPzeLZzzYNTWEBZEhV8TuiSONR4AzZ-Q_DsbhbDkZbP5OaL-eszfkS2nYaS_rb5iQYi2sjNWX_54bDzo-1XgZMV1S9V-kq69xPHKVntPlTSB7q_cbl6XXYx")


# SEARCH BY LOCATION TEXT AND TERM
response = yelp_api.search_query(location='columbus, oh', sort_by='rating', limit=1) 

# WRITE THE RESULTS OF THE API CALL TO A NEW FILE WHERE EACH BUISNESS WILL HAVE THEIR OWN FILE
for biz in response["businesses"]:
    # CREATE A FILE FOR THE GIVEN BUISNESS
    filename = str(biz["alias"]) + ".json"
    f = open(filename, "w")

    # GET MORE DATA ON A SPECIFIC LOCATION
    filteredResponse = yelp_api.business_query(id=biz["alias"])

    # MODIFY THE OPEN AND CLOSE TIMES FOR EVERY DAY IN THE WEEK FOR A GIVEN BUISNESS
    for time in filteredResponse["hours"][0]["open"]:
        time["start"] = int(time["start"])
        time["end"] = int(time["end"])

    # WRITE THE RESULTS TO THE BUISNESS' FILE
    f.write(json.dumps(filteredResponse, indent=4))
    f.close()

    # PUSH THE FILE TO DISCOVERY
    pushToDiscovery.upload_to_discovery(filename)
    # DELETE THE RETRIEVED JSON FILE 
    os.remove(filename)