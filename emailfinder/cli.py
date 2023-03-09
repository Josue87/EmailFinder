import sys
import argparse
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
    parser.add_argument('-f', '--outfile', help="Specify filename to output results", required=False)
    parser.add_argument('-v','--version', help="Show Emailfinder version", action='version', version=__version__)
    parser.add_argument('-x', '--nobanner', help="Hide banner", required=False,action='store_false')

    args = parser.parse_args()
    if args.nobanner:
        from emailfinder.utils.banner import show_banner
        show_banner()

    try:
        processing(args.domain, args.proxy, args.outfile)
    except KeyboardInterrupt:
        print("[-] EmailFinder has been interrupted. ")

if __name__ == '__main__':
    main(sys.argv[1:])