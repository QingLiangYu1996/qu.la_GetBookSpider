# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BookSpiderPipeline(object):
    
    
    def open_spider(self,spider):
    	#global result
    	self.result=dict()

    def process_item(self, item, spider):
        #创建文件

       # with open(item['name']+'-'+item['author']+'.txt', 'w', encoding='utf-8') as f:
       #     pass


        if item['name'] not in self.result:
            self.result[item['name']]={item['num']:item}
        else:
            self.result[item['name']].update({item['num']:item})

        
        return item

    def close_spider(self,spider):
        for k in self.result:
            for i in range(len(self.result[k])):
                with open(self.result[k][i]['name']+'-'+self.result[k][i]['author']+'.txt', 'a', encoding='utf-8') as f:
                    f.write(self.result[k][i]['chapter_name']+'\n'+self.result[k][i]['content']+'\n')
