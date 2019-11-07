import dist_func

CBUS_COORD = {"latitude": 39.95901, "longitude": -82.99869}

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

def coordRule(distance, aCoord=CBUS_COORD):
    # Miles -> diff in lat/long
    lat_diff = dist_func.convertToLat(distance)
    long_diff = dist_func.convertToLong(distance)

    # print('Diff\nLatitude: ' + str(lat_diff))
    # print('Longitude: ' + str(long_diff))
    
    # Builds rules for distance restrictions
    lat1 = buildRule('coordinates.latitude', aCoord['latitude']-lat_diff, '>=')
    lat2 = buildRule('coordinates.latitude', aCoord['latitude']+lat_diff, '<=')
    long1 = buildRule('coordinates.longitude', aCoord['longitude']-long_diff, '>=')
    long2 = buildRule('coordinates.longitude', aCoord['longitude']+long_diff, '<=')

    # compiles 4 rules for distance restrictions
    coordRule = groupRule(andRule(andRule(lat1, lat2), andRule(long1, long2)))
    
    return coordRule