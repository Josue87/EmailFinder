<h1 align="center">
  <b>EmailFinder</b>
  <br>
</h1>
<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python"> 
  </a>
   <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
    <img src="https://img.shields.io/badge/license-GNU-green.svg?style=square&logo=gnu">
   <a href="https://twitter.com/JosueEncinar">
    <img src="https://img.shields.io/badge/author-@JosueEncinar-orange.svg?style=square&logo=twitter">
  </a>
</p>


<p align="center">
EmailFinder is designed to find company emails that are filtered by search engines. This is done by searching for @company.com. The goal has to be to have the minimum amount of emails in the search engines.
</p>
<br/>


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

```
emailfinder -d domain.com -p http://127.0.0.1:8080
```

Parameters:
* d: Specifies the target domain.
* v: Show EmailFinder version.
* p: HTTP proxy server URL.

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
