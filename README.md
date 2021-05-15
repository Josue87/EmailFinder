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
> pip3 install emailfinder
```

Upgrades are also available using:

```
> pip3 install emailfinder --upgrade
```

## Search Engines

* google: Ok (note cookies policy and Captcha!).
* bing: OK.
* baidu: OK (few requests).
* bing: Hunting Robots very fast.

## Usage 

EmailFinder can be used in 2 ways:

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

## Example

![image](https://user-images.githubusercontent.com/16885065/118242513-b71e1800-b49d-11eb-82ab-f311ec0bba2c.png)

# Author

This project has been developed by:

* **Josué Encinar García** -- [@JosueEncinar](https://twitter.com/JosueEncinar)


# Disclaimer!

The software is designed to check a company's emails found in the search engines. The author is not responsible for any illegitimate use.
