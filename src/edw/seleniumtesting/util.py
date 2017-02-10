import argparse

from zope.component import queryUtility
from zope.component import getAllUtilitiesFor

from selenium import webdriver

from edw.seleniumtesting import indicators
from edw.seleniumtesting import charts
from edw.seleniumtesting import dataset
from edw.seleniumtesting import ITestSuite


ARG_TESTS = {
    'indicators': indicators.suite,
    'charts': charts.suite,
    'dataset': dataset.suite,
}


DRIVERS = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox,
    'phantomjs': webdriver.PhantomJS,
    'edge': webdriver.Edge,
    'ie': webdriver.Ie,
    'safari': webdriver.Safari,
}


MSG_UNKNOWN_TEST = (
    'Unknown test "{}"! '
    'Known tests: "{known_tests}"'
)


def get_browser(name, path=None):
    browser = DRIVERS[name]
    return browser(executable_path=path) if path else browser()


def validate_test_name(test_name):
    suite = queryUtility(ITestSuite, name=test_name)
    known_tests = getAllUtilitiesFor(ITestSuite)
    assert suite, MSG_UNKNOWN_TEST.format(
        test_name, known_tests=', '.join([
            s.utility_name for s in known_tests]
        )
    )


def build_cli_arguments() -> argparse.ArgumentParser:
    known_tests = [s.utility_name for s in getAllUtilitiesFor(ITestSuite)]
    parser = argparse.ArgumentParser(
        description=(
            'Run tests on websites.\n'
            'The given browser webdriver must be in your $PATH\n'
            'or given via the --browserpath option.\n\n'
            'E.g.: chrome: chromedriver, firefox: geckodriver, '
            'edge: MicrosoftWebDriver.exe.'
        )
    )
    parser.add_argument(
        'url', type=str,
        help='Site url, eg: https://digital-agenda-data.eu.'
    )
    parser.add_argument(
        'test', nargs='*', type=str,
        default=known_tests,
        help='Test names, one or more of: "{}". Default: all'.format(
            ', '.join([s.utility_name for s in known_tests])
        )
    )
    parser.add_argument('-v', '--verbose', action='count', default=1)
    parser.add_argument(
        '-B', '--browser', default='chrome',
        help='Browser to use, known: "{}". Default: chrome'.format(
            ', '.join(DRIVERS.keys())
        )
    )
    parser.add_argument(
        '-P', '--browserpath', default=None,
        help='Custom path to browser executable.'
    )

    parser.add_argument(
        '-sw', '--screenwidth', default=1024,
        help='Screen width. Default: 1024.'
    )

    parser.add_argument(
        '-sh', '--screenheight', default=768,
        help='Screen height. Default: 768.'
    )

    return parser
