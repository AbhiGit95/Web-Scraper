import scrapy
from ..items import MelbournescrapperItem


#business name, Address(street address, City, Zip, State), phone number, industry, open hours
class melspider(scrapy.Spider):
    name = 'melbourne'
    start_urls = ['https://concreteplayground.com/melbourne/shops']

    def parse(self, response):
        base_url = "https://concreteplayground.com/melbourne/shops?page={0}"
        for page in range(1, 9):
            yield scrapy.Request(base_url.format(page), dont_filter=True, callback=self.parse_page)


    def parse_page(self, response):
        list_urls = response.css("p.name a").xpath("@href").extract()
        for url in list_urls:
            yield scrapy.Request(url, callback=self.parse_subpage)

    def parse_subpage(self, response):
        items = MelbournescrapperItem()
        #business_name = response.css("div.title-container h1.title").xpath("text()").extract_first()
        industry = response.css("div.title-container a.category-title").xpath("text()").extract()
        items['Industry_name'] = industry[0].strip()
        items['Address'] = response.css("section").xpath("text()")[3].extract()
        items['Phone_num'] = response.xpath('//span/a/text()').re(r'\(?\d[- \d()]*\d')
        #response.css("span a").xpath("text()")[-1].extract()
        #response.xpath('//span/a/text()').re(r'\(?\d[- \d()]*\d') - update with this
        items['Current_day'] = response.css("p.day").xpath("text()").extract_first()
        items['Operational_hours'] = response.css("p.time").xpath("text()").extract_first()
        items['Business_name'] = response.css("div.title-container h1.title").xpath("text()").extract_first()
        #items['Industry_name'] = industry
        #items['Address'] = address
        #items['Phone_num'] = phone
        #items['Current_day'] = day
        #items['Operational_hours'] = hours
        yield items
        #command - scrapy crawl melbourne -o melb_2.csv


