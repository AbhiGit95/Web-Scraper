# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MelbournescrapperItem(scrapy.Item):
    Business_name = scrapy.Field()
    Address = scrapy.Field()
    Phone_num = scrapy.Field()
    Industry_name = scrapy.Field()
    Current_day = scrapy.Field()
    Operational_hours = scrapy.Field()
