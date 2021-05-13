from emailfinder import __version__
from random import choice
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from pyfiglet import Figlet


author = "@JosueEncinar"
description = "Search emails from a domain through search engines."
usage_example = "emailfinder -d domain.com"


def show_banner():
    fonts = ["graffiti", "smshadow", "standard", "cosmic", "speed", "epic"]
    custom_banner = Figlet(font=choice(fonts))
    banner = custom_banner.renderText("eFnDR")
    print_formatted_text(f"{banner}")
    print(f"|_ Author: {author}")
    print(f"|_ Description: {description}")
    print(f"|_ Version: {__version__}")
    print(f"|_ Usage: {usage_example}")
    print("")
