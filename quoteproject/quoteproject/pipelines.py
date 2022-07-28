# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


#Dont forget to add your pipeline to the ITEM_PIPELINES setting
#See: https://doc.scrapy.prg/en/latest/topics/item-pipelines.html

#Scraped data -> Item Containers ->json/csv files
#Scraped data -> Item Containers ->Pipeline ->SQL/Mongo database

import pymongo



class QuoteprojectPipeline:

    def __init__(self):
        self.conn=pymongo.MongoClient(
            "localhost",
            27017
        )
        db=self.conn['myquotes']
        self.collection=db['quotes_db']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
