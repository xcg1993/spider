import ssl
from http.client import HTTPResponse
from urllib.request import urlopen, Request
import csv

from chardet import detect
from lxml import etree


ssl._create_default_https_context=ssl._create_unverified_context
url='https://www.qiushibaike.com/text/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
}
def start_spider(url):
    resp=urlopen(Request(url,headers=headers))
    if resp.code==200:
        print('下载成功')
        parse(resp)
    else:
        print('失败')
def parse(resp:HTTPResponse):
    try:
        html=resp.read()
        charset=detect(html)            #detect检测给定字节串的编码
        # html=html.decode(encoding=charset)
    except:
        #如果网页编码不是utf-8的或者IS08859-1的时候，如gbk，gb2312

        content_type=resp.headers.get('Content-Type')
        mime_type,charset=tuple(content_type.split(';'))
        if charset:
            html = resp.read().decode(encoding=charset)

        else:
            html = resp.read().decode(encoding='gbk')

    et=etree.HTML(html)
    article_divs=et.xpath('//div[starts-with(@class,"article")]')
    for article_div in article_divs:
        author=article_div.xpath('./div[1]//img')
        # print(type(author),author)
        if author:
            author_name=author[0].xpath('./@alt')[0]
            author_src='https:'+author[0].xpath('./@src')[0]
            text=article_div.xpath('./a[1]//span/text()')
            text=''.join(text)
            info={
                'author_name':author_name,
                'author_photo':author_src,
                'text':text
            }
            item_pipeline(**info)




def item_pipeline(**data):
    with open('qb.csv','a') as f:
        writer=csv.DictWriter(f,fieldnames=('author_name','author_photo','text'))
        writer.writerow(data)
        print('写入成功')


def read_csv(filename):
    with open(filename,'rt') as f:
        reader=csv.DictReader(f,fieldnames=('author_name','author_photo','text'))
        for row in reader:
            print(row.values())
if __name__ == '__main__':
    start_spider(url)
    # read_csv('qb.csv')