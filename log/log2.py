import logging
from logging.handlers import HTTPHandler
from unittest import TestCase

logging.getLogger().setLevel(logging.INFO)
logging.getLogger('xcg').setLevel(logging.DEBUG)


class TestLogger(TestCase):
    # def test1(self):
    #     logging.error('--hi,info--')
    #
    # def test2(self):
    #     logger=logging.getLogger('xcg')
    #     logger.error('hi,error')
    #     logger.debug('hi,debug')

    # def test3(self):
    #     logging.basicConfig(format='[%(asctime)s ][%(levelname)s]: %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename='testlog.log',filemode='a')
    #     logger=logging.getLogger('xcg')
    #     logger.info('hi,xcginfo')



    def test4(self):
        logger=logging.getLogger('xcg')
        log_format_str='[%(asctime)s ][%(levelname)s]: %(message)s'
        log_format_date='%Y-%m-%d %H:%M:%S'
        handler=logging.StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date))
        logger.addHandler(handler)


        handler2=logging.FileHandler('handler.log')
        handler2.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date))
        handler2.setLevel(logging.WARN)
        logger.addHandler(handler2)


        httpHandler=HTTPHandler(host='127.0.0.1:5000',url='/upload_log/',method='POST')
        httpHandler.setLevel(logging.INFO)
        httpHandler.setFormatter(logging.Formatter(fmt=log_format_str,datefmt=log_format_date))
        logger.addHandler(httpHandler)
        logger.error('hi,error')
        logger.warning('hi,warning')
