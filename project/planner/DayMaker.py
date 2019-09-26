# CSE 5914 Capstone Project
# Group: Ctrl+Alt+Defeat
# Application: DayMaker

import config
import os
import json
import mvp_event

## Function definitions

# Main function (called when "python DayMaker.py" is run)
def main():

    # List where (index = hour * 4 + minute/15)
    dayList = [-1] * 96

    runTests(dayList)

def scheduleBounds(start, finish, dayList):
        dayList[timeConvert(start)] = 'The start of your day!'
        dayList[timeConvert(finish)] = 'The end of your day!'


# Given an index in the List, converts it to properly formatted military time
def indexConvert(i):
    return str(int(i/4)) + ':' + str(i%4*15).zfill(2)

# Given properly formatted military time string, converts it to an index in the dayList
def timeConvert(time):
    t = time.split(':')
    return int(int(t[0])*4 + int(t[1])/15)


# called before scheduleEvent so that changes to time are reflected
def clearEvent(event_obj, dayList):
    r = range(timeConvert(event_obj.start), timeConvert(event_obj.end))
    for i in r:
        dayList[i] = -1

# Adds an event id to dayList based on time
def scheduleEvent(event_obj, dayList):
    r = range(timeConvert(event_obj.start), timeConvert(event_obj.end))
    for i in r:
        dayList[i] = event_obj.getDetail('name') + ' Event id:' + str(event_obj.id)

# creates and returns an Mvp_event object
def createEvent(item, start, end):
    my_event = mvp_event.Mvp_event(item, start, end)
    return my_event

# Queries discovery data base using natural language query
def natLangQuery(queryStr = 'restaurant', num_results=1):
    my_query = config.discovery.query(config.environment_id,
                            config.collection_id,
                            count=num_results,
                            natural_language_query=queryStr)
    return json.loads(json.dumps(my_query.result, indent=2))

# retrieve property of json results from a query
def specifyItem(data_dict, index=0):
    return data_dict['results'][index]

# display (property) of each result to console
def viewResults(data_dict, key='name'):
    for num, item in enumerate(data_dict['results'], start=1):
        print("Option {}: {}".format(num, item[key]))

# Queries discovery data base using natural language query
def natLangQuery(queryStr = 'restaurant'):
    my_query = config.discovery.query(config.environment_id,
                            config.collection_id,
                            count=1,
                            natural_language_query=queryStr)
    return my_query

# Test function
def runTests(dayList):
    
    ## TESTS ##
    scheduleBounds('17:00', '2:30', dayList)
    print(indexConvert(50))
    print(timeConvert('12:30'))

    # test case variables
    search_term = 'ice cream'
    property_key = 'name'
    start_time = '20:00'
    end_time = '23:30'

    # natural language query and results 
    my_json = natLangQuery(search_term, 5)
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
    for x in range(len(dayList)):
        if (dayList[x] != 1):
                print(indexConvert(x) + ' - ' + str(dayList[x]))

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
    print('Your updated schedule:')
    for x in range(len(dayList)):
        if (dayList[x] != 1):
            print(indexConvert(x) + ' - ' + str(dayList[x]))

        

# Calls the main function
if __name__== "__main__" : 
    main()