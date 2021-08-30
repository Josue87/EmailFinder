from emailfinder.utils.finder import google
from emailfinder.utils.finder import bing
from emailfinder.utils.finder import baidu
from emailfinder.utils.finder import yandex
from emailfinder.utils.color_print import print_error, print_ok
from concurrent.futures import ThreadPoolExecutor, as_completed


SEARCH_ENGINES_METHODS = {
        "google": google.search,
        "bing": bing.search,
        "baidu": baidu.search,
        "yandex": yandex.search
}


def _search(engine, target, proxy_dict):
    emails = None
    print(f"Searching in {engine}...")
    try:
        emails = SEARCH_ENGINES_METHODS[engine](target, proxies=proxy_dict)
        print_ok(f"{engine} done!")
    except Exception as ex:
        print_error(f"{engine} error {ex}")
    return emails

def _get_emails(target, proxy_dict):
    threads = 4
    emails = set()
    with ThreadPoolExecutor(max_workers=threads) as executor:
        future_emails = {executor.submit(_search, engine, target, proxy_dict): engine for engine in SEARCH_ENGINES_METHODS.keys()}
        for future in as_completed(future_emails):
            try:
                data = future.result()
                if data:
                    emails = emails.union(data)
            except Exception as ex:
                print_error(f"Error: {ex}")
    return list(emails)

def processing(target, proxies):
    """
        If proxies is specified, define proxy_dict
    """
    proxy_dict = None

    if proxies:
        print('Using Proxies')
        proxy_dict = {
            "http"  : proxies,
            "https" : proxies
        }

    emails = _get_emails(target, proxy_dict=proxy_dict)
    total_emails = len(emails)
    emails_msg = f"\nTotal emails: {total_emails}"
    print(emails_msg)
    print("-" * len(emails_msg))
    if total_emails > 0:
        for email in emails:
            print(email)
    else:
        print("0 emails :(. Closing...")
