import unittest

from edw.seleniumtesting.common import BrowserTestCase


def suite(browser, base_url):
    """ Run with https://google.com/ncr to avoid language change.
    """
    # setup a new suite
    suite = unittest.TestSuite()

    # Iterate over defined tests and add them to the suite.
    # This is useful if you want to run the same tests on
    # multiple urls starting from the initial page.
    # For example searching Google and running the TestCase tests
    # on each of the results:
    #
    # for result in results:
    #     for name in GoogleTestCase.my_tests():
    #        suite.addTest(GoogleTestCase(name, browser, result.url)

    for name in GoogleTestCase.my_tests():
        testcase = GoogleTestCase(name, browser, base_url)
        suite.addTest(testcase)

    return suite


class GoogleTestCase(BrowserTestCase):

    def setUp(self):
        self.browser.get(self.url)

    def test_search_button_exists(self):
        """ 'Google Search' button exists.
        """
        selector = '//*[@value="Google Search"]'
        elements = self.browser.find_elements_by_xpath(selector)
        self.assertGreater(len(elements), 0)

