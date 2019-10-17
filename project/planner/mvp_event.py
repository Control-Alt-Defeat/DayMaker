# Class that represents a scheduled event
class Mvp_event():
    
    # Constructor
    def __init__(self, place, start, end):
        self.id = id(self)
        self.place = place
        self.start = start
        self.end = end

    # retrieve detail from json
    def getDetail(self, key='name'):
        return self.place[key]

    # change the time the event should be scheduled
    def changeTime(self, start_time, end_time):
        self.start = start_time
        self.end = end_time
    
    # change the place the event is scheduled at
    def changePlace(self, new_place):
        self.place = new_place