# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NeweggItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    itemID = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    rating = scrapy.Field()
    number_rating = scrapy.Field()
    price = scrapy.Field()
    ship = scrapy.Field()
    image_url = scrapy.Field()
    product_des = scrapy.Field()