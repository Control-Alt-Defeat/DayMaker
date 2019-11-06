from selenium import webdriver
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

homepage = "http://127.0.0.1:8000"

class PageTestCase(StaticLiveServerTestCase):

    # TODO: Fix all these tests when webpage is working again

    #def setUp(self):
        #options = Options()
        #options.add_argument('-headless')
        #self.driver = webdriver.Firefox(firefox_options=options)
        #self.driver.implicitly_wait(5)
        #self.driver.maximize_window()

    def testNavigateToPage(self):
        # TODO: Fix this test when webpage is working again
        # self.driver.get(homepage)
        pass

    #TODO: Add tests for all functionality on page
    #def tearDown(self):
        #self.driver.quit()

class EventFinderTestCase(LiveServerTestCase):

    def setUp(self):
        #self.selenium = webdriver.Chrome('tests/chromedriver.exe')
        self.selenium = WebDriver()
        super(EventFinderTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(EventFinderTestCase, self).tearDown()

    def test_empty_search(self):
        selenium = self.selenium
        # Opening the link we want to test
        import pdb; pdb.set_trace
        selenium.get(f'{homepage}/planner/plan')
        # Get number of expected results
        result_count = selenium.find_element_by_id('id_result_count').getAttribute("value")
        # find submit button
        selenium.find_element_by_id('id_find_event').click()

    def test_basic_search(self):
        selenium = self.selenium
    
        # Opening the link we want to test
        selenium.get(f'{homepage}/planner/plan')

        loc_type_el = selenium.find_element_by_id('id_loc_type').getAttribute("value")
        price_el = selenium.find_element_by_id('id_price').getAttribute("value")
        min_rating_el = selenium.find_element_by_id('id_min_rating').getAttribute("value")
        #transportation_el = selenium.find_element_by_id('id_transportation').getAttribute("value")
        start_time_el = selenium.find_element_by_id('id_start_time').getAttribute("value")
        end_time_el = selenium.find_element_by_id('id_end_time').getAttribute("value")
        
        # Get number of expected results
        result_count = selenium.find_element_by_id('id_result_count').getAttribute("value")
        
        import pdb; pdb.set_trace()
        # find submit button
        selenium.find_element_by_id('id_find_event').click()
        