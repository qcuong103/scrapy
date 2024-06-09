import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://vnexpress.net/phap-luat']

    def parse(self, response):
        for h3 in response.css('div.ss-content article h4'):
            yield {'link': h3.css('a::attr(href)').get()}

        for h4 in response.css('h4.title-news'):
            yield {'link': h4.css('a::attr(href)').get()}