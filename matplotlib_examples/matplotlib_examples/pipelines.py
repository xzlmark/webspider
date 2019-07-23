# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import basename,dirname,join


class MatplotlibExamplesPipeline(object):

    def process_item(self, item, spider):
        return item

# 修改文件名和路径
'''
urlparse模块主要是用于解析url中的参数,对url按照一定格式进行拆分或拼接
urlparse.urlparse:将url分为6个部分，返回一个包含6个字符串项目的元组：
协议、位置、路径、参数、查询、片段。
ParseResult(scheme='https', netloc='i.cnblogs.com', path='/EditPosts.aspx', params='', 
query='opt=1', fragment='')
其中 scheme 是协议  netloc 是域名服务器  path 相对路径  params是参数，query是查询的条件
'''
class MyFilesPipeline(FilesPipeline):
    def file_path(self,request,response=None,info=None):
        path = urlparse(request.url).path
        return join(basename(dirname(path)),basename(path))

'''
str='https://matplotlib.org/examples/animation/animate_decay.html'
path = urlparse(str).path    # 结果为： /examples/animation/animate_decay.html
print('path====%s' % path)

print('dirname(path)==%s' % dirname(path))  # 输出为：/examples/animation
print('basename(path)====%s ' % basename(path)) # 输出为:animate_decay.html
print(join(basename(dirname(path)),basename(path)))  输出为：animation\animate_decay.html
'''