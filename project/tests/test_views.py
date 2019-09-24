from selenium import webdriver
from django.test import TestCase

homepage = "http://localhost:8000/"
class PageTestCase(TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()


    def testNavigateToPage(self):
        self.driver.get(homepage)
        pass

    def tearDown(self):
        self.driver.quit()
