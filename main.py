import scrapy

class ScoresSpider(scrapy.Spider):
    name = 'scores'
    start_urls = [
        'https://www.matchendirect.fr/live-score/',
    ]

    def parse(self, response):
        for quote in response.css('div.panel.panel-info'):
            yield {
                'competition': quote.css('a::text').get(),
                'time' : quote.css('td.lm1::text').get(),
                'status' : quote.css('td.lm2::text').get(),
                'home-team' : quote.css('span.lm3_eq1::text').get(),
                'score' : quote.css('span.lm3_score::text').get(),
                'away-team' : quote.css('span.lm3_eq2::text').get(),
            }

