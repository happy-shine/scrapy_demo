# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    kind = scrapy.Field()
    title = scrapy.Field()
    ggtype = scrapy.Field()
    name = scrapy.Field()
    m_id = scrapy.Field()
    platform_code = scrapy.Field()
    platform_name = scrapy.Field()
    tm1 = scrapy.Field()
    areacode = scrapy.Field()
    areaname = scrapy.Field()
    protype_text = scrapy.Field()
    protype = scrapy.Field()
    m_data_source = scrapy.Field()
    m_tm = scrapy.Field()
    m_project_type = scrapy.Field()
    tm = scrapy.Field()
    is_new = scrapy.Field()
