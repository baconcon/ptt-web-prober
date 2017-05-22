#!/usr/bin/env python
# coding=utf8

import os, sys
import time
#import pprint

from crawler import *

BOARD = 'Hsinchu'
title_keyword = u'[贈送]'
INTERVAL = 600

print 'Init PttWebCrawler'
c = PttWebCrawler(board=BOARD)

latest_timestamp = -1
while True:
    c.getArticles(start_end=(-2, -1))
    result = c.get()

    articles = result.get('articles')

    #print type(result)
    #print(len(articles) ,type(articles))
    #pp = pprint.PrettyPrinter(indent=4)

    for article in articles:
        try:
            date = time.strptime(article.get('date', ''), '%a %b %d %H:%M:%S %Y')
        except ValueError:
            print 'Parse article timestamp fail, datestring:%s' % article.get('date', '')
            continue

        article_epoch = time.mktime(date)
        if article_epoch > latest_timestamp:
            # update latest_timestamp
            latest_timestamp = article_epoch

            if title_keyword in article.get('article_title', ''):
                #pp.pprint(article)
                print article.get('article_title')

    time.sleep(INTERVAL)
