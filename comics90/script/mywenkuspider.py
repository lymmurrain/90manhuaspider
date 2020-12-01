import requests

from lxml import etree
import re

class BaiduWK(object):
    def __init__(self, url):
        self.title = None
        self.url = url
        self.docType = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)'
        }



    def get_result(self):
        try:
            # 获取源码
            source_html =requests.get(self.url, headers=self.headers).content
            # 解析源码
            content = source_html.decode('gbk')
            # 获取文档类型
            self.docType = re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]
            # 获取文档标题
            self.title = re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]
            self.result= etree.HTML(content).xpath('//div[@class="bd doc-reader"]/div//text()')[0]
        except:
            return '出现异常，请稍后再试'

url = 'https://wenku.baidu.com/view/bedd4a6f2f60ddccda38a0dd.html'

WK = BaiduWK(url=url)