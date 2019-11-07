# CSE 5914 Capstone Project
# Group: Ctrl+Alt+Defeat
# Application: DayMaker

import config
import os
import json
import mvp_event
import rules

## Function definitions

# Adds bounds to schedule
def scheduleBounds(start, finish, dayList):
        start_index = timeConvert(start)
        end_index = timeConvert(finish)
        dayList[start_index] = -2
        dayList[end_index] = -3
        if (end_index < start_index):
            for i in range(0, end_index):
                dayList[i] = 0
            for j in range(start_index+1, len(dayList)):
                dayList[j] = 0
        else:
            for i in range (start_index+1, end_index):
                dayList[i] = 0


# Given an index in the List, converts it to properly formatted military time
def indexConvert(i):
    return str(int(i/4)) + ':' + str(i%4*15).zfill(2)

# Given properly formatted military time string, converts it to an index in the dayList
def timeConvert(time):
    t = time.split(':')
    return int(int(t[0])*4 + int(t[1])/15)

# called before scheduleEvent so that changes to time are reflected
def clearEvent(event_obj, dayList):
    if (timeConvert(event_obj.start) > timeConvert(event_obj.end)):
        r = range(timeConvert(event_obj.start), len(dayList))
        m = range(0, timeConvert(event_obj.end))
        for k in m:
            dayList[k] = 0
    else:
        r = range(timeConvert(event_obj.start), timeConvert(event_obj.end))
    for i in r:
        dayList[i] = 0

# Adds an event id to dayList based on time
def scheduleEvent(event_obj, dayList):
    if (timeConvert(event_obj.start) > timeConvert(event_obj.end)):
        m = range(0, timeConvert(event_obj.end))
        r = range(timeConvert(event_obj.start), len(dayList))
        for k in m:
            if dayList[k] == 0:
                dayList[k] = event_obj.getDetail('name') + ' Event id:' + str(event_obj.id)
    else:
        r = range(timeConvert(event_obj.start), timeConvert(event_obj.end))

    for i in r:
        if dayList[i] == 0:
            dayList[i] = event_obj.getDetail('name') + ' Event id:' + str(event_obj.id)

# creates and returns an Mvp_event object
def createEvent(item, start, end):
    my_event = mvp_event.Mvp_event(item, start, end)
    return my_event

# Queries discovery data base using natural language query
def natLangQuery(queryStr = '', query_filter = '', num_results=100, distance=100, aCoord=rules.CBUS_COORD):

    if (query_filter == ''):
        query_filter = rules.coordRule(distance, aCoord)
    else:
        query_filter = rules.andRule(query_filter, rules.coordRule(distance, aCoord))

    my_query = config.discovery.query(config.environment_id,
                            config.collection_id,
                            count=num_results,
                            filter=query_filter,
                            natural_language_query=queryStr)
    return json.loads(json.dumps(my_query.result, indent=2))

# retrieve property of json results from a query
def specifyItem(data_dict, index=0):
    return data_dict['results'][index]

# display (property) of each result to console
def viewResults(data_dict, key='name'):
    aliases = []
    for num, item in enumerate(data_dict['results'], start=1):
        print("Option {}: {}".format(num, item[key]))

# return an array of ALL tags
def getTags():
    tag_json = natLangQuery('', '', 1000)
    tags = []
    for num, item in enumerate(tag_json['results'], start=1):
        for tag in item['categories']:
            if (tag['title'],tag['title']) not in tags:
                tags.append((tag['title'],tag['title']))
    tags.sort()
    return tags

def printSchedule(dayList):
    start_index = dayList.index(-2)
    for x in range(start_index, len(dayList)):
        if (not isinstance(dayList[x], int) or dayList[x] > -1):
            print(indexConvert(x) + ' - ' + str(dayList[x]))
        elif (dayList[x] == -2):
            print(indexConvert(x) + ' - The start of your day!')
        elif (dayList[x] == -3):
            print(indexConvert(x) + ' - The end of your day!')

    for j in range(start_index):
        if (not isinstance(dayList[j], int) or dayList[j] > -1):
            print(indexConvert(j) + ' - ' + str(dayList[j]))
        elif (dayList[j] == -3):
            print(indexConvert(j) + ' - The end of your day!')