#!/usr/bin/env python
# coding=utf8

import os, sys
import time
#import pprint

from crawler import *

BOARD = 'Hsinchu'
#BOARD = 'Gossiping'
title_keyword = u'[贈送]'
#title_keyword = u'[問卦]'
INTERVAL = 600

print 'Init PttWebCrawler'
c = PttWebCrawler(board=BOARD)

first = True
latest_timestamp = -1
while True:
    page_index = -1
    c.getArticles(start_end=(page_index, page_index))
    result = c.get()

    matched_articles = []
    articles = result.get('articles')

    #print type(result)
    #print(len(articles) ,type(articles))
    #pp = pprint.PrettyPrinter(indent=4)

    while True:
        latest_timestamp_of_page = -1
        for article in articles:
            try:
                date = time.strptime(article.get('date', ''), '%a %b %d %H:%M:%S %Y')
            except ValueError:
                #print 'Parse article timestamp fail, datestring:%s' % article.get('date', '')
                pass

            article_epoch = time.mktime(date)
            if article_epoch > latest_timestamp:
                # update latest_timestamp_of_page
                if article_epoch > latest_timestamp_of_page:
                    latest_timestamp_of_page = article_epoch

                if title_keyword in article.get('article_title', ''):
                    #pp.pprint(article)
                    #print article.get('article_title')
                    matched_articles.append(article)
            else:
                found_old_article = True

        if first:
            first = False
            break
        elif found_old_article:
            break
        else:
            page_index = page_index-1
            c.getArticles(start_end=(page_index, page_index))
            result = c.get()
            articles = result.get('articles')

    for article in matched_articles:
        print article.get('article_title')

    # update latest_timestamp
    latest_timestamp = latest_timestamp_of_page
    time.sleep(INTERVAL)

