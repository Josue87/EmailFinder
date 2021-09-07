import requests
from random import randint
from emailfinder.utils.agent import user_agent
from emailfinder.utils.file.email_parser import get_emails
from emailfinder.utils.color_print import print_info, print_ok


def search(target, total=350, proxies=None):
	bing_count = 50
	emails = set()
	url = f"https://www.bing.com/search?q=inbody:'@{target}'&count={bing_count}"
	try:
		count = 0
		iter_count = int(total/bing_count)
		if (total%bing_count) != 0:
			iter_count +=1
		while count < iter_count:
			this_count = count*bing_count + 1
			new_url = url + f"&first={this_count}&FORM=PERE"
			response = requests.get(new_url,
				headers=user_agent.get(randint(0, len(user_agent)-1)),
				timeout=5,
				verify=False,
				proxies=proxies
			)
			text = response.text
			emails = emails.union(get_emails(target, text))
			count += 1
	except:
		pass

	emails = list(emails)
	if len(emails) > 0:
		print_ok("Bing discovered {} emails".format(len(list(emails))))
	else:
		print_info("Bing did not discover any email IDs")
	return emails
