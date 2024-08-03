## Урок 6. Scrapy. Парсинг фото и файлов

- Создайте новый проект Scrapy. Дайте ему подходящее имя и убедитесь, что ваше окружение правильно настроено для работы с проектом.
- Создайте нового паука, способного перемещаться по сайту www.unsplash.com. Ваш паук должен уметь перемещаться по категориям фотографий и получать доступ к страницам отдельных фотографий.
- Определите элемент (Item) в Scrapy, который будет представлять изображение. Ваш элемент должен включать такие детали, как URL изображения, название изображения и категорию, к которой оно принадлежит.
- Используйте Scrapy ImagesPipeline для загрузки изображений. Обязательно установите параметр IMAGES_STORE в файле settings.py. Убедитесь, что ваш паук правильно выдает элементы изображений, которые может обработать ImagesPipeline.
- Сохраните дополнительные сведения об изображениях (название, категория) в CSV-файле. Каждая строка должна соответствовать одному изображению и содержать URL изображения, локальный путь к файлу (после загрузки), название и категорию.

<hr>
<hr>

    - pip install Scrapy
    - scrapy startproject unsplash
    - scrapy genspider unsplash_spider www.unsplash.com
    - scrapy crawl unsplash_spider

## Измения в settings.py

    * USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    * DOWNLOAD_DELAY = 5
    * RANDOMIZE_DOWNLOAD_DELAY = True
    * ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
    * IMAGES_STORE = 'images'
    * DOWNLOADER_MIDDLEWARES = {'scrapy.downloadermiddlewares.offsite.OffsiteMiddleware': None,}
