# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.component import getGlobalSiteManager
gsm = getGlobalSiteManager()


class ITestSuite(Interface):
    """ A test suite
    """

