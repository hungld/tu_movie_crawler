# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class MovieItem(Item):
    movie_id = Field()
    name = Field()
    namevi = Field()
    rating = Field()
    description = Field()
    premiereDate = Field()
    duration = Field()
    actors = Field()
    movie_times = Field()

    # Reviews
    user = Field()
    review = Field()

    # Information fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
