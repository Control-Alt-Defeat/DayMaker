# CSE 5914 Capstone Project
# Group: Ctrl+Alt+Defeat
# Application: DayMaker

import config
import os
import json

## Function definitions

# Main function (called when "python DayMaker.py" is run)
def main():

    # List where (index = hour * 4 + minute/15)
    dayList = [-1] * 96

    runTests(dayList)

def scheduleBounds(start, finish, dayList):
        dayList[timeConvert(start)] = 0
        dayList[timeConvert(finish)] = -2


# Given an index in the List, converts it to properly formatted military time
def indexConvert(i):
    return str(int(i/4)) + ':' + str(i%4*15).zfill(2)

# Given properly formatted military time string, converts it to an index in the dayList
def timeConvert(time):
    t = time.split(':')
    return int(int(t[0])*4 + int(t[1])/15)

# Adds an event id to dayList based on time
def scheduleEvent(start, stop, id, dayList):
    r = range(timeConvert(start), timeConvert(stop))
    for i in r:
        dayList[i] = id

# Queries discovery data base using natural language query
def natLangQuery(queryStr = 'restaurant', num_results=1):
    my_query = config.discovery.query(config.environment_id,
                            config.collection_id,
                            count=num_results,
                            natural_language_query=queryStr)
    return json.loads(json.dumps(my_query.result, indent=2))

def specifyItem(data_dict, index=0, key='name'):
    return data_dict['results'][index][key]

# Test function
def runTests(dayList):
    
    ## TESTS ##
    scheduleBounds('17:00', '2:30', dayList)
    print(indexConvert(50))
    print(timeConvert('12:30'))
    scheduleEvent('20:00', '23:30', 1, dayList)
    for x in range(len(dayList)):
        if (dayList[x] != 1):
                print(indexConvert(x) + ' - ' + str(dayList[x]))
        else:
                print(indexConvert(x) + ' - ' + 'Your Concert!')

    search_term = 'ice cream'
    property_key = 'name'

    my_json = natLangQuery(search_term, 5)
    print(specifyItem(my_json, 0, property_key))

        

# Calls the main function
if __name__== "__main__" : 
    main()