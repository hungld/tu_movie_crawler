# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class MovieItem(Item):
    name = Field()
    namevi = Field()
    rating = Field()
    description = Field()
    premiereDate = Field()
    duration = Field()
    actors = Field()

    # Reviews
    user = Field()
    review = Field()

    # Information fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()


class SessionTimesItem(Item):
    group_cinema = Field()
    cinema_name = Field()
    session_times_2d = Field()
    session_times_3d = Field()
