import scrapy


class QuotesSpider(scrapy.Spider):
    name = "toscrape-xpath"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        quote_xpath = '//div[@class="quote"]/span[@class="text"]/text()'
        author_xpath = '//div[@class="quote"]/span/small[@class="author"]/text()'
        quotes = response.xpath(quote_xpath).getall()
        authors = response.xpath(author_xpath).getall()
        for quote, author in zip(quotes, authors):
            yield {
                'text': quote[1:-1],
                'author': author
            }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)