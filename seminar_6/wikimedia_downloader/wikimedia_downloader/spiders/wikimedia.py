#my user agent - узнать своего агента

# BOT_NAME: Это имя вашего бота. Например: BOT_NAME = 'my_scraper'.
# USER_AGENT: Установите пользовательский агент для вашего бота. Например: USER_AGENT = 'my_scraper (+http://www.mywebsite.com)'.
# ROBOTSTXT_OBEY: Установите True, если хотите, чтобы ваш бот соблюдал правила файла robots.txt сайтов. Например: ROBOTSTXT_OBEY = True.
# ITEM_PIPELINES: Здесь вы можете определить пайплайны для обработки собранных элементов. Например: ITEM_PIPELINES = {'myproject.pipelines.ExamplePipeline': 300}.
# IMAGES_STORE: Укажите путь для хранения скачанных изображений. Например: IMAGES_STORE = '/path/to/valid/dir'.
# DOWNLOAD_DELAY: Установите задержку (в секундах) между запросами. Например: DOWNLOAD_DELAY = 2.
# DOWNLOAD_DELAY_FACTOR: Установите коэффициент для случайной задержки. Например: DOWNLOAD_DELAY_FACTOR = 0.5.
# LOG_LEVEL: Установите уровень журналирования. Например: LOG_LEVEL = 'INFO'.

import scrapy

class WikimediaSpider(scrapy.Spider):
    name = 'wikimedia'
    start_urls = ['https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons']

    def parse(self, response):
        for image in response.xpath('//*[@id="mw-category-media"]/ul/li/div/span/a/img'):
            image_url = image.xpath('@src').extract_first()
            yield scrapy.Request(response.urljoin(image_url), self.save_image)

    def save_image(self, response):
        filename = response.url.split('/')[-1]
        # Сохраняем изображение в папку images
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)


        # # Сохраняем изображение в папку images
        # def save_image(self, response):
        #     filename = response.url.split
        #     with open(f'images/{filename}', 'wb') as f:
        #         f.write(response.body)




# class WikimediaSpider(scrapy.Spider):
#     name = 'wikimedia'
#     start_urls = ['https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons']

#     def parse(self, response):
#         # Используем XPath для извлечения URL изображений
#         for image in response.xpath('//div[contains(@class, "gallerytext)]/a/@href').extract():
#             yield scrapy.Request(response.urljoin(image), self.parse_image)

#     def parse_image(self, response):
#         # Получаем имя файла изображения
#         filename_url = response.url.split('//a[contains(@href, "/wiki/File:")]/@href').extract_first()
#         if filename_url:
#             yield scrapy.Request(response.urljoin(filename_url), self.save_image)
        
        
        
        
        

