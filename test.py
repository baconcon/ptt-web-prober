#!/usr/bin/env python

import os, sys
import pprint

from crawler import *

#OUTPUTFILE = 'output.json'
#sys.argv.extend(['--filename', OUTPUTFILE])

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='''
            A crawler for the web version of PTT, the largest online community in Taiwan.
            Input: board name and page indices (or articla ID)
            Output: BOARD_NAME-START_INDEX-END_INDEX.json (or BOARD_NAME-ID.json)
        ''')
parser.add_argument('-b', metavar='BOARD_NAME', help='Board name', required=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-i', metavar=('START_INDEX', 'END_INDEX'), type=int, nargs=2, help="Start and end index")
group.add_argument('-a', metavar='ARTICLE_ID', help="Article ID")
parser.add_argument('-f', '--filename', metavar='OUTPUT FILENAME', help="Output file name")
#parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)

args = parser.parse_args()


board = args.b
filename = args.filename if args.filename else None
start_end = (args.i[0], args.i[1]) if args.i else None
article_id = args.a if args.a else None

c = PttWebCrawler(board=board, filename=filename)

c.getArticles(start_end=start_end, article_id=article_id)

result = c.get()
print result
print type(result)

#data = c.get(OUTPUTFILE)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(data)

#os.remove(OUTPUTFILE)
