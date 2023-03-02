import scrapy
from splash.items import QuoteItem
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']

    def start_requests(self):
        url = 'http://quotes.toscrape.com/js'
        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_text = quote.css('span.text::text').get()
            quote_author = quote.css('small.author::text').get()
            quote_tags = quote.css('div.tags a.tag::text').get()
            yield QuoteItem(
                text=quote_text, author=quote_author, tags=quote_tags
            )
