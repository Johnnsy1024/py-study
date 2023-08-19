from scrapy import Selector
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Response

class JzSpider(CrawlSpider):
    name = "spider_3"
    start_urls = ["https://astrobiology.nasa.gov/missions/"]
    

    rules = (
        # Rule(LinkExtractor(allow='/missions/.+/', restrict_xpaths='//*[@id="current-missions"]/div[@class="mission-block"]'), callback="parse_1", follow=True),
        # Rule(LinkExtractor(allow='/missions/.+/', restrict_xpaths='//*[@id="future-missions"]/div[@class="mission-block"]'), callback="parse_2", follow=True),
        # Rule(LinkExtractor(allow='/missions/.+/', restrict_xpaths='//*[@id="concept-missions"]/div[@class="mission-block"]'), callback="parse_3", follow=True),
        Rule(LinkExtractor(allow='/missions/.+/', restrict_xpaths='//*[@id="past-missions"]/div[@class="mission-block"]'), callback="parse_3", follow=True),
    )
    
    def parse_1(self, response: Response):

        sel = Selector(response)
        txt_selects = sel.xpath('//div[@class="article-text"]/p//text()') # 分若干个段落
        title_selects = sel.xpath('//div[@class="col-2"]/h1//text()')
        desc_selects = sel.xpath('//div[@class="col-2"]/h2//text()')
        txt = ''
        for sec in txt_selects:
            txt += sec.extract()  
        title = title_selects.extract()
        desc = desc_selects.extract()
        yield {
            'title' : title,
            'desc' : desc,
            'content' : txt
        }
    def parse_2(self, response: Response):
        sel = Selector(response)
        txt_selects = sel.xpath('//div[@class="article-text"]/p//text()') # 分若干个段落
        title_selects = sel.xpath('//div[@class="col-2"]/h1//text()')
        desc_selects = sel.xpath('//div[@class="col-2"]/h2//text()')
        txt = ''
        for sec in txt_selects:
            txt += sec.extract()  
        title = title_selects.extract()
        desc = desc_selects.extract()
        yield {
            'title' : title,
            'desc' : desc,
            'content' : txt
        }
        
    def parse_3(self, response: Response):
        sel = Selector(response)
        txt_selects = sel.xpath('//div[@class="article-text"]/p//text()') # 分若干个段落
        title_selects = sel.xpath('//div[@class="col-2"]/h1//text()')
        desc_selects = sel.xpath('//div[@class="col-2"]/h2//text()')
        txt = ''
        for sec in txt_selects:
            txt += sec.extract()  
        title = title_selects.extract()
        desc = desc_selects.extract()
        yield {
            'title' : title,
            'desc' : desc,
            'content' : txt
        }
