# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num=scrapy.Field()
    name=scrapy.Field()
    author=scrapy.Field()
    content=scrapy.Field()
    chapter_name=scrapy.Field()
    

