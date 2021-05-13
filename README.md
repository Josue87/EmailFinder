![Supported Python versions](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square&logo=gnu)

# **EmailFinder - search emails through Search Engines**

```
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


```

## Installation:

```
> python3 setup.py bdist_wheel
> pip3 install dist/emailfinder-0.1b0.tar.gz 
```


## Search Engines

* google: Ok (note cookies policy and Captcha!).
* bing: OK.
* baidu: OK (few requests).
* bing: Hunting Robots very fast.

## Usage 

```
> emailfinder -d domain.com
```

### CLI
```
emailfinder -d domain.com
```

Parameters:
* d: Specifies the target domain.
* v: Show EmailFinder version.

### In code
```
from emailfinder.extractor import *


emails1 = get_emails_from_google("domain.com")
emails2 = get_emails_from_bing("domain.com")
emails3 = get_emails_from_baidu("domain.com")
```

# Author

This project has been developed by:

* **Josué Encinar García** -- [@JosueEncinar](https://twitter.com/JosueEncinar)


# Disclaimer!

The software is designed to leave no trace in the documents we upload to a domain. The author is not responsible for any illegitimate use.
