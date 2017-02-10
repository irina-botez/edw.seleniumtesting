import unittest

from zope.interface import implementer

from edw.seleniumtesting import ITestSuite
from edw.seleniumtesting import gsm
from edw.seleniumtesting.common import BrowserTestCase


@implementer(ITestSuite)
class TestSuite(object):

    utility_name = 'edw.seleniumtesting.google'

    def __call__(self, browser, base_url):
        suite = unittest.TestSuite()
        for name in GoogleTestCase.my_tests():
            testcase = GoogleTestCase(name, browser, base_url)
            suite.addTest(testcase)
        return suite


gsm.registerUtility(TestSuite(), name=TestSuite.utility_name)


class GoogleTestCase(BrowserTestCase):

    def setUp(self):
        self.browser.get(self.url)

    def test_search_button_exists(self):
        """ 'Google Search' button exists.
        """
        selector = '[value="Google Search"]'
        self.browser.find_elements_by_css_selector(selector)
