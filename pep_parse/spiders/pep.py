import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (ALLOWED_DOMAINS,
                                START_URLS,
                                SPIDER_NAME)


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_links = response.xpath(
            '//section[@id="numerical-index"]'
            '//a[@class="pep reference internal"]/@href').getall()
        for link in all_links:
            if not link.endswith('/'):
                link += '/'
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        _, number, _, *name = response.css('h1.page-title::text').get().split()
        data = {
            'number': number,
            'name': ' '.join(name).strip(),
            'status': response.css('dt:contains("Status") + dd ::text').get(),
        }

        yield PepParseItem(data)
