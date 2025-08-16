import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    # start_urls - это та ссылка, от которой начинается парсинг
    start_urls = ["https://www.divan.ru/category/svet"]
    # start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        # Пишем ту же команду, которую писали в терминале
        svets = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным cdtnbkmybrjv в списке
        for svet in svets:
            # Используем новый для нас оператор "yield", который помогает обрабатывать одно отдельное действие
            # С его помощью мы можем управлять потоком выполнения, останавливать и возобновлять работу парсера
            # С другими операторами мы такого делать не можем
            yield {
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.pY3d2 span::text').get(),
                'url': svet.css('a').attrib['href']
            }

