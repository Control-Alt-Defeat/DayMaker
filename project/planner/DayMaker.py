# CSE 5914 Capstone Project
# Group: Ctrl+Alt+Defeat
# Application: DayMaker

from . import config
import os
import json
from . import mvp_event

## Function definitions

# Main function (called when "python DayMaker.py" is run)
def main():

    # List where (index = hour * 4 + minute/15)
    dayList = [-1] * 96

    # Function that runs tests on startup
    ############################ REMOVE LINE COMMENT TO RUN TESTS ON EXECUTION ###################################
    # runTests(dayList)

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
def natLangQuery(queryStr = '', query_filter = '' , num_results=50):
    my_query = config.discovery.query(config.environment_id,
                            config.collection_id,
                            count=num_results,
                            filter=query_filter,
                            natural_language_query=queryStr)
    return json.loads(json.dumps(my_query.result, indent=2))

# Rule building functions
def buildRule(field, value, operator='::'):
    my_rule = field+operator+str(value)
    return my_rule

def defineRule(my_filter=''):
    return my_filter

def andRule(rule1, rule2):
    new_rule = rule1 + ',' + rule2
    return new_rule

def orRule(rule1, rule2):
    new_rule = rule1 + '|' + rule2
    return new_rule

def groupRule(rule):
    new_rule = '(' + rule + ')'
    return new_rule

# def buildQuery(query_filter = '', num_results=50):
#     my_filter = buildRule('price', "\"$\"")
#     print(my_filter)
#     my_query = config.discovery.query(config.environment_id,
#                             config.collection_id,
#                             count=num_results,
#                             filter=query_filter,
#                             natural_language_query=queryStr)
#     return json.loads(json.dumps(my_query.result, indent=2))

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

# Test function
def runTests(dayList):
    
    ## TESTS ##
    scheduleBounds('17:50', '2:30', dayList)
    print('####################  [Welcome to DayMaker]  #########################\n')
    # printSchedule(dayList)
    # print(indexConvert(50))
    # print(timeConvert('12:30'))

    # test case variables
    property_key = 'name'
    start_time = '20:00'
    end_time = '23:30'

    # prints the array of all tags
    print('ALL TAGS: {}\n'.format(getTags()))

    print('What kind of event would you like to schedule?')
    search_term = input()

    # # limit options by number
    # print('How many options would you like to choose from?')
    # results_num = input()

    # creates filter for query ('::' - 'is' operator by default)
    rule1 = buildRule('review_count', '\"189\"', '::')
    rule2 = buildRule('price', '\"$\"', '::')
    rule3 = buildRule('rating', 4.5, '::')
    group_rule = groupRule(andRule(rule2, rule3))
    my_filter = orRule(rule1, group_rule)

    ################### ADD LINE COMMENT BELOW TO APPLY FILTER ##########################
    my_filter = ''

    print('Filtering \"' + search_term + '\" options by ' + my_filter + '\nResults:\n')

    # natural language query and results
    my_json = natLangQuery(search_term, my_filter)
    viewResults(my_json)

    # user choice
    print('Enter a number for the event you would like to schedule:')
    user_choice = int(input()) - 1

    # user time specification
    print('Would you like to set a custom time for your event at', specifyItem(my_json, user_choice)[property_key], '? y/n:')
    user_input = input()
    if user_input.find('y') != -1:
        print('When would you like to arrive? Enter in the format of hh:mm')
        start_time = input()
        print('When would you like to leave? Enter in the format of hh:mm:')
        end_time = input()

    # creates event object
    event_obj = createEvent(specifyItem(my_json, user_choice), start_time, end_time)
    # schedules event obj
    scheduleEvent(event_obj, dayList)

    # prints entire schedule
    # start_index = dayList.index('The start of your day!')
    # for x in range(start_index, len(dayList)):
    #     if (dayList[x] != -1):
    #             print(indexConvert(x) + ' - ' + str(dayList[x]))

    # for x in range(start_index):
    #     if (dayList[x] != -1):
    #             print(indexConvert(x) + ' - ' + str(dayList[x]))

    printSchedule(dayList)

    # event_obj.changePlace() method test
    print('would you like to change the place of your event? id:', event_obj.id, ' y/n:')
    user_choice = input()
    if user_choice.find('y') != -1:
        print('would you like to change the place of this event? select a new place:')
        viewResults(my_json)
        print('Enter a number for the place you would like to switch to instead:')
        user_choice = int(input()) - 1
        new_place = specifyItem(my_json, user_choice)
        event_obj.changePlace(new_place)

    # event_obj.changeTime() method test
    print('would you like to change the time of your event? id: ', event_obj.id, ' y/n:')
    user_choice = input()
    if user_choice.find('y') != -1:
        print('new start time? hh:mm')
        start_time = input()
        print('new end time? hh:mm')
        end_time = input()
        
    clearEvent(event_obj, dayList)
    event_obj.changeTime(start_time, end_time)
    scheduleEvent(event_obj, dayList)

    # reprints schedule in case changes were made
    print('Your event starts at ' + event_obj.start)
    print('Your updated schedule:')
    printSchedule(dayList)

        

# Calls the main function
if __name__== "__main__" : 
    main()
