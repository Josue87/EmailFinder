import requests
import urllib3
from time import sleep
from random import randint
from emailfinder.utils.exception import YandexDetection
from emailfinder.utils.agent import user_agent
from emailfinder.utils.file.email_parser import get_emails
from emailfinder.utils.color_print import print_info, print_ok


urllib3.disable_warnings()

def search(target, total=50, proxies=None):
	old_text = ""
	num_results = 50 if total >= 50 else total
	emails = set()
	base_url = "https://www.yandex.com/search/?"
	total_loop = int(total/num_results)
	if (total%num_results) != 0:
		total_loop += 1
	count = 1
	old_useragent = -1
	total_timeout = 0
	while count <= total_loop:
		while True:
			next_useragent = randint(0, len(user_agent)-1)
			if next_useragent != old_useragent:
				break
		old_useragent = next_useragent
		new_url = base_url + f'text=inbody:"%40{target}"&numdoc={num_results}&p={count-1}&lr=10435'
		try:
			new_agent = user_agent.get(count, next_useragent)
			response = requests.get(new_url,
				headers=new_agent,
				timeout=5,
				verify=False,
				proxies=proxies
			)
			text = response.text
			if old_text == text:
				break
			old_text = text
			if "robot are sending requests" in text:
				total_timeout += 1
				if total_timeout == 3:
					raise YandexDetection
				sleep(2)
				continue
			emails = emails.union(get_emails(target, text))
		except Exception as ex:
			raise ex #It's left over... but it stays there
		count += 1
	emails = list(emails)
	if len(emails) > 0:
		print_ok("Yandex discovered {} emails".format(len(list(emails))))
	else:
		print_info("Yandex did not discover any email IDs")
	return emails
