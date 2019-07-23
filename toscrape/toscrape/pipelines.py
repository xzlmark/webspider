# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 将得到的字母转换为数字星级
class ToscrapePipeline(object):
    # 定义一个字典，存储星级的对应关系 
    review_rating_map = {
        'One':1,
        'Two':2,
        'Three':3,
        'Four':4,
        'Five':5
    }
    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.review_rating_map[rating]
        return item
