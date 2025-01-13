import json
import random
import scrapy
from ..items import AmazonItem  



class ProductSpider(scrapy.Spider):
    name = "product"
    allowed_domains = ["www.amazon.com"]

    def __init__(self, search=None, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.search = search.replace(' ', '+')
        self.user_agents = self.get_user_agents_list()

    def get_user_agents_list(self):
        with open('amazonscraper/amazonscraper/spiders/user_agents.json', 'r') as file:
            return json.loads(file.read())

    def start_requests(self):
        start_url = f'https://www.amazon.com/s?k={self.search}'
        yield scrapy.Request(url=start_url, callback=self.parse,
                             headers={"User-Agent": self.user_agents[random.randint(0, len(self.user_agents)-1)]})

    def parse(self, response):
        for item in response.css('div[role="listitem"][data-component-type="s-search-result"]'):
            yield self.parse_amazon_item(item)

        next_page = response.xpath('//a[text()="Next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_amazon_item(self, item):
        amazon_item = AmazonItem()
        amazon_item['title'] = item.css('div[data-cy="title-recipe"] a > h2 > span::text').get()
        amazon_item['price'] = item.css('div[data-cy="price-recipe"] a span.a-price span::text').get()
        amazon_item['stars'] = item.css('div[data-cy="reviews-block"] i[data-cy="reviews-ratings-slot"] span::text').get()
        amazon_item['num_reviews'] = item.css('div[data-cy="reviews-block"] span[data-component-type="s-client-side-analytics"] span::text').get()
        amazon_item['image'] = item.css('img.s-image::attr(src)').get()
        return amazon_item
