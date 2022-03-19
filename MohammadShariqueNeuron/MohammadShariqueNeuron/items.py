# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class MohammadshariqueneuronItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Price                        =scrapy.Field()
    Title                        =scrapy.Field()
    Stock                        =scrapy.Field()
    Manufacturer                 =scrapy.Field()
    Review                       =scrapy.Field()
    Description                  =scrapy.Field()
    Delivery_Info                =scrapy.Field()
    
    

