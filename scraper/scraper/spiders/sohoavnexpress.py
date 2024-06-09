# -*- coding: utf8 -*-
from abc import ABC

import scrapy
import csv

class SohoaVnexpressNet(scrapy.Spider):
    name = "sohoa"
    start_urls = [
        'https://vnexpress.net/phap-luat',
    ]
    file = open("output.csv", "w", newline="")
    writer = csv.DictWriter(file, fieldnames=["keys", "link"])
    writer.writeheader()

    def start_requests(self):
        # urls = [
        #     'https://vnexpress.net/phap-luat',
        # ]
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for title in response.css("h4.title-news a, h4.title-news a"):
            link = title.css("::attr(href)").get()
            print("link: " + str(link))

            self.writer.writerow({"keys" : link})
            # yield scrapy.Request(link, callback=self.parse_article)

    def parse_article(self, response):
        artilce = {
            'title': response.xpath('//h1[@class="title-detail"]/text()').extract()[0].strip(),
            'description': response.xpath('//p[@class="description"]/text()').extract()[0].strip(),
            'content': response.xpath('//p[@class="Normal"]').extract()[0].strip(),
            'author': response.xpath('//article[@class="fck_detail "]/p[@style="text-align:right;"]/strong/text() | //p[@class="author_mail"]/strong/text() | //article[@class="fck_detail "]/p[@style="text-align:right;"]/em/text() | //article[@class="fck_detail "]/p/strong/text()').extract()[0].strip(),
            'publish_date': response.xpath('//span[@class="date"]/text()').extract()[0].strip()}
        # for key, text in artilce.items():
        #     print ("{key}: {text}".format(key = key.upper(), text = text))

        return artilce
