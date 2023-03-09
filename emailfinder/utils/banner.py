from emailfinder import __version__
from random import choice
from prompt_toolkit import print_formatted_text
from pyfiglet import Figlet

author = "@JosueEncinar"
maintainer = "Irvine,CA"
description = "Search emails from a domain through search engines."
usage_example = "emailfinder -d example.com"

def show_banner():
    fonts = ["graffiti", "smshadow", "standard", "cosmic", "speed", "epic"]
    custom_banner = Figlet(font=choice(fonts))
    banner = custom_banner.renderText("eFnDR")
    print_formatted_text(f"{banner}")
    BannerInfo=( f"|_ Author: {author}\n"
    f"|_ Maintained By: {maintainer}\n"
    f"|_ Description: {description}\n"
    f"|_ Version: {__version__}\n"
    f"|_ Usage: {usage_example}" )
    print(BannerInfo)