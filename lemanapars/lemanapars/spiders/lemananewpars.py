import scrapy
# "https://novosibirsk.lemanapro.ru"    https://novosibirsk.lemanapro.ru/catalogue/lampochki

class LemananewparsSpider(scrapy.Spider):
    name = "lemananewpars"
    allowed_domains = ["https://novosibirsk.lemanapro.ru"]
    # start_urls - это та ссылка, от которой начинается парсинг
    start_urls = ["https://novosibirsk.lemanapro.ru/catalogue/lampochki"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        # Пишем ту же команду, которую писали в терминале
        lamps = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным диваном в списке
        for lamp in lamps:
            # Используем новый для нас оператор "yield", который помогает обрабатывать одно отдельное действие
            # С его помощью мы можем управлять потоком выполнения, останавливать и возобновлять работу парсера
            # С другими операторами мы такого делать не можем
            yield {
                'name': lamp.css('div.lsooF span::text').get(),
                'price': lamp.css('div.pY3d2 span::text').get(),
                'url': lamp.css('a').attrib['href']
            }

