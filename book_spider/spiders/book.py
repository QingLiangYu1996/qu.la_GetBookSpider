# -*- coding: utf-8 -*-
import scrapy
import re
import copy
from book_spider.items import BookSpiderItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['www.qu.la']
    start_urls = [
        "https://www.qu.la/book/204000/",
        "https://www.qu.la/book/142577/"\
        ]

    def parse(self, response):
        #初始化item对象
        book_item=BookSpiderItem()

        #书名
        book_item['name']=response.css('#info > h1 ::text').extract()[0]
        #作者
        book_item['author']=re.search(r'：(.*)',response.css('#info > p:nth-child(2) ::text').extract()[0]).group(1)


        for i in range(len(response.css('#list > dl > dt:nth-child(14)~dd'))):
            try:
                book_item['num']=i
                yield scrapy.Request(response.url+re.search('/(\d{6,8})\.html"',response.css('#list > dl > dt:nth-child(14)~dd').extract()[i]).group(1)+'.html',\
                    meta={'book_item':copy.deepcopy(book_item)},callback=self.parse_content)
            except:
                continue


    def parse_content(self,response):
        #章节名
        book_chapter_name=response.css('#wrapper > div.content_read > div.box_con > div.bookname > h1 ::text').extract()[0]
        #章节内容
        book_content=''
        for i in range(len(response.css('#content ::text').extract())):
            book_content+=response.css('#content ::text').extract()[i]+'\n'
        
        book_item=response.meta['book_item']

        book_item['chapter_name']=book_chapter_name
        book_item['content']=book_content



        yield book_item


