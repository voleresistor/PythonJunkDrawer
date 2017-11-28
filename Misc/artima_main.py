'''
Testing main() function as explained in 2003 by Guido van Rossum
at:
https://www.artima.com/weblogs/viewpost.jsp?thread=4829

-h, --help      Print this help
-t[] --toot[]   Print number of toots specified
'''
import sys
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def toot_count(toots):
    '''
    Return number of toots!
    '''
    try:
        res = int(toots)
    except:
        return 1
    return res

def main(argv=None):
    # parse command line options
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ht:", ["help", "toot="])
        except(getopt.error) as msg:
            raise Usage(msg)
        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print(__doc__)
                return 0
            elif o in ("-t", "--toot"):
                print("Toot! " * toot_count(a))
                return 0
        # process arguments
        for arg in args:
            print(arg)
    except(Usage) as err:
        print(err.msg)
        print("for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
