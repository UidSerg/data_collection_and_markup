from typing import Any
import scrapy
from scrapy.http import Response
import os
import csv


class UnsplashSpiderSpider(scrapy.Spider):
    name = "unsplash_spider"
    allowed_domains = ['www.unsplash.com', 'images.unsplash.com']
    start_urls = ["https://www.unsplash.com"]

    def parse(self, response):
        """функция прохода по каталогам"""
        for page in response.xpath('//div[@class="qaAX1"]/ul//a/@href').extract():
            page_name=page.split('/')[-1]
            # для стартовой страницы назовем каталог Photo
            if page_name == "":
                page_name = 'Photo'
            # print(response.urljoin(page))
            yield scrapy.Request(response.urljoin(page), self.parse_page, meta={'page_name': page_name})
            

    def parse_page(self, response):
        """функция прохода по картинкам в категории"""
        page_name = response.meta['page_name']
        for image in response.xpath('//div[@class="JM3zT"]/a/div/img[2]'):
            image_url = image.xpath('@srcset').extract_first()
            urls = image_url.split('?')[0]
            image_name = image.xpath('@alt').extract_first()
            yield scrapy.Request(urls, self.save_image, meta={'page_name': page_name, 'image_name': image_name})


    def save_image(self, response):
        """функция сохранения"""
        page_name = response.meta['page_name']
        filename = response.meta['image_name']
        # filename = response.url.split('/')[-1]
        # проверим есть ли папка если папки нет создадим
        page_dir = f'images/{page_name}'
        if not os.path.exists(page_dir):
            os.makedirs(page_dir)
        
        # Сохраняем изображение в папку images
        local_url = f'images/{page_name}/{filename}.jpg'
        with open(local_url, 'wb') as f:
            f.write(response.body)

        # Сохраняем изображение в images_data.csv
        csv_file = 'images_data.csv'
        csv_exists = os.path.exists(csv_file)
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not csv_exists:
                writer.writerow(['URL', 'local_url', 'Category', 'Name'])
            writer.writerow([response.url, local_url, page_name, filename])
