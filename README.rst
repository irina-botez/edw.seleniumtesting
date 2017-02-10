===================
edw.seleniumtesting
===================

Selenium based automated testing.


Installation
------------
This package requires **Python 3.5**!
::

    $ pip install -U https://github.com/eaudeweb/edw.seleniumtesting/archive/master.zip
    $ seleniumtesting -h



Usage
-----

To run the ``test1``, ``test2`` and ``test3`` tests in Firefox,
specifying the path to ``geckodriver`` at the default ``1024x768`` resolution: ::

    $ seleniumtesting -v -B firefox -P /usr/bin/geckodriver https://localhost test1 test2 test3


To run all tests in phantomjs in glorious 4K resolution: ::

    $ seleniumtesting -v -B phantomjs -P /usr/bin/phantomjs -sw 3840 -sh 2160 https://localhost

Failed tests and tests that encounter an error will save a screenshot in the current working directory.


Contribute
----------

- Issue Tracker: https://github.com/eaudeweb/edw.seleniumtesting/issues
- Source Code: https://github.com/eaudeweb/edw.seleniumtesting
- Documentation: https://github.com/eaudeweb/edw.seleniumtesting/wiki


License
-------

The project is licensed under the GPLv3.
