# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ExcelPipeline:
    def __init__(self):
        self.data = []

    def process_item(self, item, spider):
        self.data.append(item)
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.data)
        df.to_excel('output.xlsx', index=False)
