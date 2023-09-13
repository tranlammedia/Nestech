import scrapy
from .items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        # 'https://quotes.toscrape.com'
        'https://quotes.toscrape.com/page/1'
    ]
    
    page_number = 2
    
    def parse(self, response, **kwargs):
        
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

        # next_page = response.css('li.next a::attr(href)').get()
        
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        
        next_page = 'https://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)
        
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
            
            