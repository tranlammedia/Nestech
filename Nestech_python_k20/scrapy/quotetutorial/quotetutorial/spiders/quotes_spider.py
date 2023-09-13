import scrapy
from scrapy.http import FormRequest
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        # 'https://quotes.toscrape.com'
        'https://quotes.toscrape.com/login'
        # 'https://quotes.toscrape.com/page/1'
    ]
    
    def start_scraping(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css("div.quote")
        
        for quote in all_div_quotes:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tag = quote.css(".tag::text").extract()
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            yield items

        next_page = response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.start_scraping)

    def parse(self, response, **kwargs):
        token = response.css('form input::attr(value)').extract_first()
        print(token)
        return FormRequest.from_response(response=response,formdata={
            "csrf_token": token,
            "username": "hello",
            "password": "123"
        }, callback=self.start_scraping)
            
        