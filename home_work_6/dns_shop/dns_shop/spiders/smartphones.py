import scrapy

class SmartphonesSpider(scrapy.Spider):
    name = "smartphones"
    allowed_domains = ["dns-shop.ru"]
    start_urls = ["https://www.dns-shop.ru/catalog//smartfony/"]

    def parse(self, response):
        # Парсинг названий смартфонов
        for product in response.css('.catalog-product__name'):
            yield {
                'name': product.css('::text').get().strip()
            }

        # Пагинация
        next_page = response.css('a.pagination-widget__page-link_next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

