# 从python:3.8.2 镜像开始构建
FROM python:3.8.2
# 维护者
MAINTAINER lymmurrain
# 将爬虫文件复制到/root目录下
ADD ./comics90 /root/
# 安装依赖
RUN pip3 install  -i https://pypi.doubanio.com/simple/  scrapy
RUN pip3 install pymongo -i https://pypi.doubanio.com/simple/
RUN pip3 install  -i https://pypi.doubanio.com/simple/ pillow
RUN pip3 install  -i https://pypi.doubanio.com/simple/ scrapy_redis
# 将工作目录移到 /root/comics90/script
WORKDIR /root/comics90/script
# 启动容器时使用命令 python start.py 开始爬虫
CMD ["python", "start.py"]