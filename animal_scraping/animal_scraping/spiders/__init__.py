# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from animal_scraping.items import AnimalScrapingItem

from animal_scraping.items import AnimalScrapingItem
 
class AnimalSpider(CrawlSpider):
    name = 'animal_spider'
    allowed_domains = ['egida.by']
    start_urls = ['https://egida.by/cruelty/']
    rules = (
        Rule(LinkExtractor(allow=('cruelty', )), callback='parse'),
    )
 
    def parse(self, response):
        item = AnimalScrapingItem()
        item['announcement_url'] = response.url
        item['title'] = response.xpath("//h3[@class='entry__title']/text()").get()
        item['description'] = response.xpath("//meta[@itemprop='description']/@content").get()
        item['date'] = response.xpath("//ul[@class='single-entry__mini-details']/li/text()").get()
        return item