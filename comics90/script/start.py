from scrapy.cmdline import execute
# 单机爬取全站
# execute("scrapy crawl comic".split())
#分布式爬取全站

execute("scrapy crawl crawl90".split())

#只爬取单个漫画
# execute("scrapy crawl crawl90".split())

