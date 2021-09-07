import requests
from random import randint
from bs4 import BeautifulSoup
from emailfinder.utils.exception import GoogleCaptcha, GoogleCookiePolicies
from emailfinder.utils.agent import user_agent
from emailfinder.utils.file.email_parser import get_emails
from emailfinder.utils.color_print import print_info, print_ok


def search(target, proxies=None, total=200):
	emails = set()
	start = 0
	num = 50 if total > 50 else total
	iterations = int(total/num)
	if (total%num) != 0:
		iterations += 1
	url_base = f"https://www.google.com/search?q=intext:@{target}&num={num}"
	cookies = {"CONSENT": "YES+srp.gws"}
	while start < iterations:
		try:
			url = url_base + f"&start={start}"
			response = requests.get(url,
				headers=user_agent.get(randint(0, len(user_agent)-1)),
				allow_redirects=False,
				cookies=cookies,
				verify=False,
				proxies=proxies
			)
			text = response.text
			if response.status_code == 302 and ("htps://www.google.com/webhp" in text or "https://consent.google.com" in text):
				raise GoogleCookiePolicies()
			elif "detected unusual traffic" in text:
				raise GoogleCaptcha()
			emails = emails.union(get_emails(target, text))
			soup = BeautifulSoup(text, "html.parser")
			# h3 is the title of every result
			if len(soup.find_all("h3")) < num:
				break
		except Exception as ex:
			raise ex #It's left over... but it stays there
		start += 1
	emails = list(emails)
	if len(emails) > 0:
		print_ok("Google discovered {} emails".format(len(list(emails))))
	else:
		print_info("Google did not discover any email IDs")
	return emails
