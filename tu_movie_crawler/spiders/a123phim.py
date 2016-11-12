# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
# from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from tu_movie_crawler.items import MovieItem, SessionTimesItem

import datetime
import scrapy
import socket
import urlparse


class A123phimSpider(scrapy.Spider):
    name = "123phim"
    allowed_domains = ["123phim.vn"]

    start_urls = [
            'http://www.123phim.vn/phim/',
            'http://www.123phim.vn/phim/sap-chieu/',
            ]

    mc = MapCompose(lambda i: urlparse.urljoin('http://123phim.vn', i))

    def parse(self, response):
        # Get item URLs and yield Requests
        url_selector = response.xpath('//*[@class="block-base movie"]/a[1]/@href')
        for url in url_selector.extract():
            yield Request(self.mc(url)[0], callback=self.parse_item)

    def parse_item(self, response):
        """ This function parses a movie page

        @url http://www.123phim.vn/phim/840-lich-chieu-doctor-strange.html
        @returns items 1
        @scrapes name namevi rating description premiereDate duration actors
        @scrapes url project spider server date
        """
        l = ItemLoader(item=MovieItem(), response=response)

        l.add_xpath('name', '//*[@class="filmDescription"]/h3/text()')
        l.add_xpath('namevi', '//*[@class="filmDescription"]/h2/text()')
        l.add_xpath('rating',
                    '//*[@class="icon imdb"]/strong/text()', TakeFirst())
        l.add_xpath('description', '//*[@class="filmShortDesc"]/text()')
        l.add_xpath('premiereDate',
                    '//*[@class="publish-date-block"]/span/text()',
                    TakeFirst(), re='(\d+/\d+)')
        l.add_xpath('duration',
                    '//*[@class="filmInfo"]/span[1]/text()',
                    TakeFirst(), re='(\d+)')
        l.add_xpath('actors', '//*[@class="titleItemSmall"]/a/text()')

        # Information fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()

    # def parse_session_times(self, response):
    #     item = SessionTimesItem()
    #     item['group_cinema'] = response.xpath(
    #             '//*[@class="titgroupCinema"]/div/text()').extract()
    #     item['cinema_name'] = response.xpath(
    #             '//*[@class="titItemCinema"]/div/text()').extract()
    #     # item['session_times_2d'] = response.xpath('')
    #     return item
