from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

homepage = "http://localhost:8000/"
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
