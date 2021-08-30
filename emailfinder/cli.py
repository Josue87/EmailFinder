import sys
import argparse
from emailfinder.utils.banner import show_banner
from emailfinder.core import processing
from emailfinder import __version__


def main(argv=None):
    """The entry point for the script

   Args:
       argv (list): The list of parameters passed.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--domain', help="Domain to search",required=True)
    parser.add_argument('-p', '--proxy', help="HTTP proxy server URL", required=False)
    parser.add_argument('-v','--version', help="Show Emailfinder version", action='version', version=__version__)

    args = parser.parse_args()
    show_banner()

    # limit = 200

    try:
        processing(args.domain, args.proxy)
    except KeyboardInterrupt:
        print("[-] EmailFinder has been interrupted. ")


if __name__ == '__main__':
    main(sys.argv[1:])
