# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HelloWorldDemoPipeline:
    def process_item(self, item, spider):
        print(f'process_item is {item}')
        with open('../result.txt', 'a') as fp:
            fp.write(item.title)
            fp.write('\t')
            fp.write(item.score)
            fp.write('\t')
            fp.write(item.motto)
            fp.write('\n')
        return item
