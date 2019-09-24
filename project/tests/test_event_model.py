from django.test import TestCase
from planner.models import Event

class EventTestCase(TestCase):

    #Test functionality of constructor
    def testCreateEvent(self):
        #TODO: Update for newer model
        event = Event("ExEvent",1234)
        self.assertEqual(event.title, "ExEvent", "Event name creation failed.")
        self.assertEqual(event.id, 1234, "Event id creation failed.")


    def testUpdateEventTime(self):
        #TODO: Use setUp method to create event, and assert that the model can be updated
        pass

    #Add more updates for fields that are added
    
    def testLoadData(self):
        #TODO: write test to feed sample yelp input to create an event
        pass
