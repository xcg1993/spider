import logging
import time
from logging.handlers import HTTPHandler
from unittest import TestCase



"""
CRITICAL = 50=FATAL   严重错误
ERROR = 40              错误
WARNING = 30=WARN       警告
INFO = 20              普通信息
DEBUG = 10              调试信息
NOTSET = 0              默认，没有
"""

#获取日志记录器，并且设置记录器的等级为INFO
#getlogger(name)   name表示日志记录器的名称
#name为空，即没有指定，默认为root
logging.getLogger().setLevel(logging.INFO)
logging.getLogger('disen').setLevel(logging.DEBUG)

class TestLogger(TestCase):
    #单元测试方法是以‘test’开头的
    def test1(self):
        logging.error('--hi,info--')


    def test2(self):
        logger=logging.getLogger('disen')
        logger.info('--disen hi,info--')
        logger.error('--disen hi,error--')
        logger.critical('--disen hi,critical--')

    def test3(self):
        #设置日志格式   formatter
        #设置root日志记录器的格式
        """
        日志格式化常用的变量:
            asctime   时间
            name   记录器
            levelname   等级名称
            funcName
            pathname
            message

        """

        logging.basicConfig(format='[%(asctime)s ][%(levelname)s]: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',   #设置asctime的格式
                            filename='test.log',     #输出日志的文件名
                            filemode='a')               #将日志的消息以追加的方式加入到文件中
        logger = logging.getLogger('disen')
        logger.info('--disen hi,info--')
        logger.error('--disen hi,error--')
        logger.critical('--disen hi,critical--')

    def test4(self):
        # formatter、logger和handler关系
        # handler对象可以添加formatter
        # logger可以添加多个handler  如果没有添加handler默认会添加一个StreamHandler（控制台打印的）
        # 常用的处理器handler有哪些
        #  1、StreamHandler    控制台打印的输出处理器
        #  2、FileHandler   日志文件输出的处理器
        #  3、HttpHandler   网络上传日志的处理器
        logger=logging.getLogger('disen')
        log_format_str="<%(user_id)s >[ %(asctime)s ]-%(levelname)s: %(message)s"
        log_format_date='%Y-%m-%d %H:%M:%S'
        handler1=logging.StreamHandler()   #实例化handler  标准输出的
        handler1.setLevel(logging.INFO)
        handler1.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date))



        logger.addHandler(handler1)

        handler2=logging.FileHandler('handler.log')
        handler2.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date))
        handler2.setLevel(logging.WARN)     #文件处理器只记录警告信息

        logger.addHandler(handler2)
        #创建上传日志处理器
        httpHandler=HTTPHandler(host='127.0.0.1:5000',url='/upload_log/',method='POST')
        httpHandler.setLevel(logging.ERROR)
        httpHandler.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date))

        logger.addHandler(httpHandler)
        extra_info={'user_id':'1000001'}
        logger.info('hi,info',extra=extra_info)
        logger.warning('hi,warn',extra=extra_info)

        logger.error('hi,error',extra=extra_info)

    def test5(self):
        #默认的StreamHandler的level是warning
        a=logging.getLogger('aaa')
        a.setLevel(logging.INFO)

        a.error('aaaaaaaaaaaaaaaaaaa')
        


        a.addHandler(logging.StreamHandler())
        a.handlers[0].setLevel(logging.INFO)