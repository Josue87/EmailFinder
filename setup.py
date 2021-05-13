
from setuptools import setup, find_packages
from os import path
import emailfinder


long_description = """|Supported Python versions| |License|

**MetaFinder - Metadata search through Search Engines**
=======================================================

::

    _______  _______  _        ______   _______ 
    (  ____ \(  ____ \( (    /|(  __  \ (  ____ )
    | (    \/| (    \/|  \  ( || (  \  )| (    )|
    | (__    | (__    |   \ | || |   ) || (____)|
    |  __)   |  __)   | (\ \) || |   | ||     __)
    | (      | (      | | \   || |   ) || (\ (   
    | (____/\| )      | )  \  || (__/  )| ) \ \__
    (_______/|/       |/    )_)(______/ |/   \__/
                                                

    |_ Author: @JosueEncinar
    |_ Description: Search emails from a domain through search engines.
    |_ Version: 0.1b
    |_ Usage: emailfinder -d domain.com

Installation:
-------------

::

    > pip3 install emailfinder

Upgrades are also available using:

::

    > pip3 install emailfinder --upgrade

Search Engines
--------------

- google: Ok (note cookies policy and Captcha!).
- bing: OK.
- baidu: OK (few requests).
- bing: Hunting Robots very fast.

Usage
-----

CLI
~~~
::

    emailfinder -d domain.com

Parameters: 

- d: Specifies the target domain.
- v: Show EmailFinder version.


In Code
~~~~~~~

::

from emailfinder.extractor import *


emails1 = get_emails_from_google("domain.com")
emails2 = get_emails_from_bing("domain.com")
emails3 = get_emails_from_baidu("domain.com")


Author
======

This project has been developed by:

-  **Josué Encinar García** -- https://twitter.com/JosueEncinar


Disclaimer!
===========

The software is designed to leave no trace in the documents we upload to a domain. The author is not responsible for any
illegitimate use.

.. |Supported Python versions| image:: https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python
.. |License| image:: https://img.shields.io/badge/license-GNU-green.svg?style=flat-square&logo=gnu

"""

setup(
    name='emailfinder',
    version=emailfinder.__version__,
    author='Josue Encinar (@JosueEncinar)',
    description='EmailFinder - Emails search through Search Engines',
    include_package_data=True,
    license='GNU GPLv3+',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Josue87/EmailFinder",
    entry_points={
        'console_scripts': [
            'emailfinder=emailfinder.cli:main',
        ],
    },
    install_requires=[
        "requests>=2.25.1",
        "prompt-toolkit>=3.0.5",
        "urllib3>=1.26.4"
    ]
)
