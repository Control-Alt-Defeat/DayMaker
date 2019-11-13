from .DayMaker import *

def main():

    # List where (index = hour * 4 + minute/15)
    dayList = [-1] * 96

    # Function that runs tests on startup
    runTests(dayList)

# Test function
def runTests(dayList):
    
    ## TESTS ##
    DayMaker.scheduleBounds('17:50', '2:30', dayList)
    print('####################  [Welcome to DayMaker]  #########################\n')
    # printSchedule(dayList)
    # print(indexConvert(50))
    # print(timeConvert('12:30'))

    # test case variables
    property_key = 'name'
    start_time = '20:00'
    end_time = '23:30'

    # prints the array of all tags
    # print('ALL TAGS: {}\n'.format(DayMaker.getTags()))

    print('What kind of event would you like to schedule?')
    search_term = input()

    # # limit options by number
    # print('How many options would you like to choose from?')
    # results_num = input()

    # creates filter for query ('::' - 'is' operator by default)
    rule1 = DayMaker.rules.buildRule('review_count', '\"189\"', '::')
    rule2 = DayMaker.rules.buildRule('price', '\"$\"', '::')
    rule3 = DayMaker.rules.buildRule('rating', 4.5, '::')
    group_rule = DayMaker.rules.groupRule(DayMaker.rules.andRule(rule2, rule3))
    my_filter = DayMaker.rules.orRule(rule1, group_rule)

    ################### ADD LINE COMMENT BELOW TO APPLY FILTER ##########################
    my_filter = DayMaker.rules.openRule(1000, 1200, 2)

    print('Filtering \"' + search_term + '\" options by ' + my_filter + '\nResults:\n')

    # natural language query and results
    my_json = DayMaker.natLangQuery(search_term, my_filter, 100, 1, DayMaker.rules.CBUS_COORD, {'start_time':1000, 'end_time':1200, 'date':DayMaker.datetime.datetime.today()})
    # DayMaker.markOpen(my_json, 1000, 1200, DayMaker.datetime.datetime.today())
    DayMaker.viewResults(my_json)

    # user choice
    print('Enter a number for the event you would like to schedule:')
    user_choice = int(input()) - 1

    # Test for distance function
    # coord1 = DayMaker.specifyItem(my_json, 5)['coordinates']
    # coord2 = DayMaker.specifyItem(my_json, 13)['coordinates']
    # print(coord1)
    # print(coord2)
    # #lat1 = 
    # print('Distance between: ' + str(DayMaker.dist_func.distance(coord1['latitude'], coord1['longitude'], coord2['latitude'], coord2['longitude'], 'M')))

    # user time specification
    print('Would you like to set a custom time for your event at', DayMaker.specifyItem(my_json, user_choice)[property_key], '? y/n:')
    user_input = input()
    if user_input.find('y') != -1:
        print('When would you like to arrive? Enter in the format of hh:mm')
        start_time = input()
        print('When would you like to leave? Enter in the format of hh:mm:')
        end_time = input()

    # creates event object
    event_obj = DayMaker.createEvent(DayMaker.specifyItem(my_json, user_choice), start_time, end_time)
    # schedules event obj
    DayMaker.scheduleEvent(event_obj, dayList)

    # prints entire schedule
    # start_index = dayList.index('The start of your day!')
    # for x in range(start_index, len(dayList)):
    #     if (dayList[x] != -1):
    #             print(indexConvert(x) + ' - ' + str(dayList[x]))

    # for x in range(start_index):
    #     if (dayList[x] != -1):
    #             print(indexConvert(x) + ' - ' + str(dayList[x]))

    DayMaker.printSchedule(dayList)

    # event_obj.changePlace() method test
    print('would you like to change the place of your event? id:', event_obj.id, ' y/n:')
    user_choice = input()
    if user_choice.find('y') != -1:
        print('would you like to change the place of this event? select a new place:')
        DayMaker.viewResults(my_json)
        print('Enter a number for the place you would like to switch to instead:')
        user_choice = int(input()) - 1
        new_place = DayMaker.specifyItem(my_json, user_choice)
        event_obj.changePlace(new_place)

    # event_obj.changeTime() method test
    print('would you like to change the time of your event? id: ', event_obj.id, ' y/n:')
    user_choice = input()
    if user_choice.find('y') != -1:
        print('new start time? hh:mm')
        start_time = input()
        print('new end time? hh:mm')
        end_time = input()
        
    DayMaker.clearEvent(event_obj, dayList)
    event_obj.changeTime(start_time, end_time)
    DayMaker.scheduleEvent(event_obj, dayList)

    # reprints schedule in case changes were made
    print('Your event starts at ' + event_obj.start)
    print('Your updated schedule:')
    DayMaker.printSchedule(dayList)

# Calls the main function
if __name__== "__main__" : 
    main()