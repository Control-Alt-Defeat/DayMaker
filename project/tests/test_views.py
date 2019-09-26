from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

homepage = "http://localhost:8000/"
class PageTestCase(StaticLiveServerTestCase):


    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(firefox_options=options)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def testLoadPage(self):
        self.driver.get(homepage)
        self.assertEqual(self.driver.title, "DayMaker - Home", "Page does not open to homepage")

    def testDeleteEvent(self):
        self.driver.get(homepage)
        events = self.driver.find_elements(By.CLASS_NAME, 'eventStyle')
        numEvents = len(events)
        if numEvents > 0:

            #Remove event, probably should label the remove buttons
            events[0].find_element(By.TAG_NAME, 'button').click()
            events = self.driver.find_elements(By.CLASS_NAME, 'eventStyle')
            self.assertEquals(numEvents, len(events) + 1, "Remove button does not function properly.")
        else:
            #Add an event to remove if needed
            self.fail("Page did not have an Event to remove")

    #TODO: Add tests for all functionality on page
    def tearDown(self):
        self.driver.quit()
