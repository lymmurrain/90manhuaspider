# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# info = {
#     'comic_name': comic_name,
#     'info': {
#         'desc': desc,
#         'new_chap': msg_lst_right[0],
#         'alias': msg_lst_right[1],
#         'status': msg_lst_right[2],
#         'theme': msg_lst_right[3],
#         'author': msg_lst_right[4],
#         'type': msg_lst_right[5],
#         'area': msg_lst_right[6],
#         'update_time': msg_lst_right[7],
#     },
#     'chap_name_list': chap_name_list
# }
class ComicItems(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    comic_name = scrapy.Field()
    info = scrapy.Field()
    chap_name_list = scrapy.Field()


# yield {
#     'img_url': img_url,
#     'img_name': img_name,
#     'meta': response.meta
# }
class PicItems(scrapy.Item):
    img_url = scrapy.Field()
    img_name = scrapy.Field()
    comic_name = scrapy.Field()
    chap_name = scrapy.Field()
    page = scrapy.Field()
