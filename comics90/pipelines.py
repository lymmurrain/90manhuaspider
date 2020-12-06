# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from twisted.internet.threads import deferToThread


class PicPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        url = item['img_url']
        yield Request(url, meta={'img_name': item['img_name'], 'img_meta': item['meta']}, dont_filter=True)

    def file_path(self, request, response=None, info=None):
        file_path = request.meta['img_name'] + '.jpg'
        return file_path


class MongoPipeline(object):

    def process_item(self, item, spider):

        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):

        if item.get('meta'):
            obj = {
                'img_url': item['img_url'], 'img_name': item['img_name'],
                'comic_name': item['meta']['comic_name'],
                'chap_name': item['meta']['chap_name'],
                'page': item['meta']['page'],
            }
            spider.client.comicSpider.picStore.insert_one(obj)
        else:
            spider.client.comicSpider.comicStore.insert_one(item)
        return item

    def close_spider(self, spider):
        spider.client.close()
