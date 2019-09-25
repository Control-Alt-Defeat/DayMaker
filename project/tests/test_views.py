from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.firefox.options import Options

homepage = "http://localhost:8000/"
class PageTestCase(TestCase):


    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(firefox_options=options)


    def testNavigateToPage(self):
        self.driver.get(homepage)
        pass

    #TODO: Add tests for all functionality on page
    def tearDown(self):
        self.driver.quit()
