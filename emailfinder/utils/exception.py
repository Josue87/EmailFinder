class GoogleCaptcha(Exception):
    def __init__(self, *args):
        self.data = "Captcha detected"
        if args:
            self.data = args[0]
    def  __str__(self):
        return "GoogleCaptcha, {0}".format(self.data)

class GoogleCookiePolicies(Exception):
    def __init__(self, *args):
        self.data = "Cookie Policy detected"
        if args:
            self.data = args[0]
    def  __str__(self):
        return "GoogleCookiePolicies, {0}".format(self.data)

class BaiduDetection(Exception):
    def __init__(self, *args):
        self.data = "Robot detected"
        if args:
            self.data = args[0]
    def  __str__(self):
        return "BaiduDetection, {0}".format(self.data)

class YandexDetection(Exception):
    def __init__(self, *args):
        self.data = "Robot detected"
        if args:
            self.data = args[0]
    def  __str__(self):
        return "YandexDetection, {0}".format(self.data)