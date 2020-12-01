import scrapy
from scrapy.http import Request
import pymongo


class ComicSpider(scrapy.Spider):
    name = 'comic'
    start_urls = ['http://m.90mh.com/list/z/{}/'.format(i) for i in range(1, 4)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, meta={'type':'multiComic'})

    def parse(self, response):
        if not response.url:
            pass
        # self.client.comicSpider.multiSuccess.insert_one({"url":response.url,'meta':response.meta})
        comic_href_list = response.xpath("//ul//a[@class='txtA']//@href").extract()
        comic_name_list = response.xpath("//a[@class='txtA']/text()").extract()
        for comic_name,comic_url in zip(comic_name_list,comic_href_list):
            yield Request(url=comic_url,callback=self.parse_comic,meta={'comic_name':comic_name,'type':'comic'})

    def parse_comic(self,response):
        if not response.url:
            pass
        chap_href_list = response.xpath("//div/div[@class='comic-chapters']/div[@class='list']/ul/li/a//@href").extract()
        chap_name_list = response.xpath("//div/div[@class='comic-chapters']/div[@class='list']/ul/li/a/span/text()").extract()
        # update_time = response.xpath("//dl[@class='pic_zi fs15'][8]/dd[@class='left']//text()").extract_first()
        msg_lst_right = response.xpath("//dl[@class='pic_zi fs15']/dd[@class='left']").xpath('string(.)').extract()
        desc = response.xpath("//p[@class='txtDesc autoHeight']//text()").extract_first()
        info = {
          'comic_name':response.meta['comic_name'],
           'info':{
                'desc':desc,
              'new_chap':  msg_lst_right[0] ,
              'alias':  msg_lst_right[1] ,
              'status':  msg_lst_right[2] ,
              'theme':  msg_lst_right[3] ,
              'author':  msg_lst_right[4] ,
              'type':  msg_lst_right[5] ,
              'area':  msg_lst_right[6] ,
              'update_time':  msg_lst_right[7] ,
           }
        }
        self.client.comicSpider.comics_z.insert_one(info)
        # for chap_name,chap_url in zip(chap_name_list,chap_href_list):
        #     chap_name = chap_name.rjust(4,'0')
        #     yield Request(url=chap_url, callback=self.parse_Pic, meta={'chap_name': chap_name, 'type': 'pic','comic_name':response.meta['comic_name'],'page':'001'})

    def parse_Pic(self,response):
        if not response.url:
            pass
        img_url = response.xpath("//mip-link/mip-img//@src").extract_first()
        img_name = response.meta['comic_name'] + r'/' + response.meta['chap_name'] + r'/' +response.meta['page']
        yield {
            'img_url': img_url,
            'img_name' : img_name,
            'meta' : response.meta

        }
        if response.meta['page'] =='001':
            tol_page = response.xpath("//span[@id='k_total']//text()").extract_first()
            sub_str = response.url.replace('.html','-{}.html')
            pic_url_list =  [sub_str.format(str(i)) for i in range(2,int(tol_page)+1)]
            current_page = 2
            for pic_url in pic_url_list:
                chap_name = response.meta['chap_name']
                page = str(current_page).rjust(3,'0')
                current_page += 1
                yield Request(url=pic_url, callback=self.parse_Pic,
                              meta={'chap_name': chap_name, 'type': 'pic', 'comic_name': response.meta['comic_name'],
                                    'page': page})




    def __init__(self,*args,**kwargs):
        self.client = pymongo.MongoClient()
        super(ComicSpider, self).__init__(*args,**kwargs)

    def closed(self):
        self.client.close()


class MyFavSpider(scrapy.Spider):
    name = 'myFavorite'
    start_urls = ['http://m.90mh.com/manhua/zhongjiangchengweini/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, meta={'comic_name':'终将成为你'})

    def parse(self,response):
        if not response.url:
            pass
        chap_href_list = response.xpath("//div/div[@class='comic-chapters']/div[@class='list']/ul/li/a//@href").extract()
        chap_name_list = response.xpath("//div/div[@class='comic-chapters']/div[@class='list']/ul/li/a/span/text()").extract()
        update_time = response.xpath("//dl[@class='pic_zi fs15'][8]/dd[@class='left']//text()").extract_first()
        self.client.comicSpider.comics.insert_one({"comic_url":response.url,'meta':response.meta,'update_time':update_time})
        for chap_name,chap_url in zip(chap_name_list,chap_href_list):
            chap_name = chap_name.rjust(4,'0')
            yield Request(url=chap_url, callback=self.parse_Pic, meta={'chap_name': chap_name, 'type': 'pic','comic_name':response.meta['comic_name'],'page':'001'})

    def parse_Pic(self,response):
        if not response.url:
            pass
        img_url = response.xpath("//mip-link/mip-img//@src").extract_first()
        img_name = response.meta['comic_name'] + r'/' + response.meta['chap_name'] + r'/' +response.meta['page']
        yield {
            'img_url': img_url,
            'img_name' : img_name,
            'meta' : response.meta

        }
        if response.meta['page'] =='001':
            tol_page = response.xpath("//span[@id='k_total']//text()").extract_first()
            sub_str = response.url.replace('.html','-{}.html')
            pic_url_list =  [sub_str.format(str(i)) for i in range(2,int(tol_page)+1)]
            current_page = 2
            for pic_url in pic_url_list:
                chap_name = response.meta['chap_name']
                page = str(current_page).rjust(3,'0')
                current_page += 1
                yield Request(url=pic_url, callback=self.parse_Pic,
                              meta={'chap_name': chap_name, 'type': 'pic', 'comic_name': response.meta['comic_name'],
                                    'page': page})




    def __init__(self,*args,**kwargs):
        self.client = pymongo.MongoClient()
        super(MyFavSpider, self).__init__(*args,**kwargs)

