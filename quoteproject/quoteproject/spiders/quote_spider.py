

#scrapy startproject quoteproject-->start

import scrapy

from ..items import QuoteprojectItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls=[
        "http://quotes.toscrape.com/"
    ]


    def parse(self,response):

        # title=response.css("title::text").extract()
        # title=response.xpath("//title/text()").extract()
        # title= response.css("li.next a").xpath("@href").extract()

        # yield {"title":title}

        items=QuoteprojectItem()    #imorted blueprint of class QuoteprojectItem()

        all_div_quotes=response.css("div.quote")

        for x in all_div_quotes:

            title=x.css('span.text::text').extract()
            author=x.css('.author::text').extract()
            tags=x.css('.tag::text').extract()
#then
            # yield {
            #     'title':title,
            #     'author':author,
            #     'tags':tags
            #     }

            #Saving your extracted data directly into dataase is quite difficult to make it easier first we put the data into temporary containers that is called items
#now
            items['title']=title
            items['author']=author
            items['tag']=tags


            yield items

        next_page=response.css('li.next a::attr(href)').get()

        if next_page is not None:   #Checking if the second page is emty or not

            yield response.follow(next_page,callback=self.parse)  #Go with this parse method gain

