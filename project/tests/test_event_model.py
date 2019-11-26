from django.test import TestCase
from planner.models import Event

class EventTestCase(TestCase):

    def setUp(self):
        self.event = Event()
        self.event.id = 1234

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
