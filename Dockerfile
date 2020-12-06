FROM python:3.8.2
MAINTAINER lymmurrain
ADD ./comics90 /root/
RUN pip3 install  -i https://pypi.doubanio.com/simple/  scrapy
RUN pip3 install pymongo -i https://pypi.doubanio.com/simple/
RUN pip3 install  -i https://pypi.doubanio.com/simple/ fake_useragent
RUN pip3 install  -i https://pypi.doubanio.com/simple/ pillow
RUN pip3 install  -i https://pypi.doubanio.com/simple/ scrapy_redis
WORKDIR /root/comics90/script
CMD ["python", "start.py"]