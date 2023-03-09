from emailfinder.utils.finder import google
from emailfinder.utils.finder import bing
from emailfinder.utils.finder import baidu
from emailfinder.utils.finder import yandex
from emailfinder.utils.color_print import print_error
from concurrent.futures import ThreadPoolExecutor, as_completed


SEARCH_ENGINES_METHODS = {
        "Google": google.search,
        "Bing": bing.search,
        "Baidu": baidu.search,
        "Yandex": yandex.search
}

def _search(engine, target, proxy_dict):
    emails = None
    print(f"Searching in {engine}...")
    try:
        emails = SEARCH_ENGINES_METHODS[engine](target, proxies=proxy_dict)
    except Exception as ex:
        print_error(f"{engine} error {ex}")
    return emails

def _get_emails(target, proxy_dict):
    emails = set()
    with ThreadPoolExecutor(max_workers=None) as executor:
        try:
            future_emails = {executor.submit(_search, engine, target, proxy_dict): engine for engine in SEARCH_ENGINES_METHODS.keys()}
            for future in as_completed(future_emails):
                try:
                    data = future.result()
                    if data:
                        emails = emails.union(data)
                except Exception as ex:
                    print_error(f"Error: {ex}")
                    # Raise the exception again in the main thread
                    raise ex
        finally:
            # Shut down the executor and wait for all tasks to complete
            executor.shutdown(wait=True)
    return list(emails)

def processing(target, proxies, outfile):
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

    if total_emails > 0:
        emails_msg = f"\nTotal emails: {total_emails}"
        print(emails_msg)
        print("-" * len(emails_msg))
        fileemails = ''
        if outfile:
            for email in emails:
                print(email)
                fileemails += email + '; '
            with open(outfile, 'a+') as file:
                file.write(fileemails)
            if outfile:
                print("\nEmails saved to ", outfile)
        else:
            for email in emails:
                print(email)
    else:
        print_error("No emails found.")
