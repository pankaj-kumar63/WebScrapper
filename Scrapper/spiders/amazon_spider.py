import scrapy


from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number=2
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1617256650&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0']

    def parse(self, response):
        item=AmazontutorialItem()                       #This item will store insance of the Amazontutorial class
        title=response.css('.a-color-base.a-text-normal::text').extract()
        author=response.css('.a-color-secondary .a-size-base.a-link-normal::text').extract()
        price=response.css('.a-spacing-top-small .a-price-whole::text').extract()
        image_link=response.css('.s-image::attr(src)').extract()

        item['title']=title      #inserting into temporary container
        item['author']=author
        item['price']=price
        item['image_link']=image_link

        yield item

        next_page='https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+str(AmazonSpiderSpider.page_number)+'&qid=1617257242&rnid=1250225011&ref=sr_pg_1'


        if AmazonSpiderSpider.page_number<=10:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)