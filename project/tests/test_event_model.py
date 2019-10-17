from django.test import TestCase
from planner.models import Event

class EventTestCase(TestCase):

    def setUp(self):
        self.event = Event("ExEvent", 1234)

    #Test functionality of constructor
    def testCreateEvent(self):
        self.assertEqual(self.event.title, "ExEvent", "Event name creation failed.")
        self.assertEqual(self.event.id, 1234, "Event id creation failed.")

    # Test addAddress function
    def testEventAddAddress(self):
        self.event.addAddress("123 North High Street")
        self.assertEqual(self.event.location, "123 North High Street", "Event.addAddress failed.")

    # Test set loc_name
    def testSetEventLocName(self):
        self.event.loc_name = "Cazuelas"
        self.assertEqual(self.event.loc_name, "Cazuelas", "Setting Event loc_name failed.")

    # Test set loc_type
    def testSetEventLocType(self):
        self.event.loc_type = "Restaurant"
        self.assertEqual(self.event.loc_type, "Restaurant", "Setting Event loc_type failed.")

    def testSetEventStartTime(self):
        self.event.start_time = "5:00pm"
        self.assertEqual(self.event.start_time, "5:00pm", "Setting Event start_time failed.")

    def testSetEventEndTime(self):
        self.event.end_time = "7:00pm"
        self.assertEqual(self.event.end_time, "7:00pm", "Setting Event end_time failed.")

    def testSetEventCost(self):
        self.event.cost = 3
        self.assertEqual(self.event.cost, 3, "Setting Event cost failed.")

    def testSetEventRating(self):
        self.event.rating = 5
        self.assertEqual(self.event.rating, 5, "Setting Event rating failed.")
        
    def testLoadData(self):
        #TODO: write test to feed sample yelp input to create an event
        pass
