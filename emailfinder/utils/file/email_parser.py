import re


def get_emails(target, text):
    regex = r"[a-zA-Z0-9_\.+-]+@" + target
    emails = re.findall(regex, text.replace("<em>", "").replace("<\em>","")
                                .replace("<strong>", "").replace("</strong>", "")
                                .replace("<b>", "").replace("</b>", ""))
    return emails

