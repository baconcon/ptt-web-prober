#!/usr/bin/env python

import os, sys

from crawler import *

OUTPUTFILE = 'output.json'

sys.argv.extend(['--filename', OUTPUTFILE])

c = PttWebCrawler()

#c.get(OUTPUTFILE)

#os.remove(OUTPUTFILE)
