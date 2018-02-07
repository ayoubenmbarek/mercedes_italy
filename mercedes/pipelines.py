# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#from scrapy.exceptions import DropItem

class MercedesPipeline(object):
    def process_item(self, item, spider):
        return item


#class DuplicatesPipeline(object):
#    def __init__(self):
#        self.ids_seen = set()
#
#    def process_item(self, item, spider):
#        if item['DEALER_ID'] in self.ids_seen:
#            raise DropItem("Duplicate item found: %s" % item)
#        else:
#            self.ids_seen.add(item['DEALER_ID'])
#            return item
