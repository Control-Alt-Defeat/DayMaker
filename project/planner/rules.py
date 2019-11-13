from .distance import convertToLat, convertToLong

CBUS_COORD = {"latitude": 39.95901, "longitude": -82.99869}

# Rule building functions
def buildRule(field, value, operator='::'):
    my_rule = field+operator+str(value)
    return my_rule

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
    lat_coord = float(aCoord['latitude'])
    long_coord = float(aCoord['longitude'])
    
    # Miles -> diff in lat/long
    lat_diff = convertToLat(distance)
    lat_diff = lat_diff if lat_coord>0 else lat_diff*-1
    long_diff = convertToLong(distance)
    long_diff = long_diff if long_coord>0 else long_diff*-1

    # Builds rules for distance restrictions
    lat1 = buildRule('coordinates.latitude', lat_coord-lat_diff, '>=')
    lat2 = buildRule('coordinates.latitude', lat_coord+lat_diff, '<=')
    long1 = buildRule('coordinates.longitude', long_coord+long_diff, '>=')
    long2 = buildRule('coordinates.longitude', long_coord-long_diff, '<=')

    # compiles 4 rules for distance restrictions
    coord_rule = groupRule(andRule(andRule(lat1, lat2), andRule(long1, long2)))
    
    return coord_rule

def openRule(start_time, end_time, day_num):

    # Builds rules for intial hours restrictions
    opening = buildRule('hours.open.start', start_time, '<=')
    closing = buildRule('hours.open.end', end_time, '>=')
    overnight = buildRule('hours.open.is_overnight', "true", '::')
    weekday = buildRule('hours.open.day', day_num, ':')

    # compiles 4 rules for hours restrictions
    open_rule = groupRule(andRule(andRule(weekday, opening), groupRule(orRule(closing, overnight))))

    return open_rule

def build_query_filter(price_val, min_rating):
    if (price_val == '1'):
        price = '$'
    elif (price_val == '2'):
        price = '$$'
    elif (price_val == '3'):
        price = '$$$' 

    price_rule, rate_rule, query_filter = None, None, None

    if price_val:
        price_rule = groupRule(buildRule('price', price, '::'))
    if min_rating:
        rate_rule = groupRule(buildRule('rating', int(min_rating), '>='))
    if price_rule and rate_rule:
        query_filter = andRule(price_rule, rate_rule)
    elif price_rule or rate_rule:
        query_filter = price_rule if price_rule else rate_rule
    else:
        query_filter = ""
    
    return query_filter