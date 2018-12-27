"""
代理设置
proxyHandler
build_opener是否支持多个Handler
"""
from http.cookiejar import CookieJar
from urllib.request import ProxyHandler, Request, build_opener, HTTPCookieProcessor

def build_browser():
    cookie_handler=HTTPCookieProcessor(CookieJar())
    proxy_handler=ProxyHandler(proxies={
        'https':'27.208.83.27:8118'
    })
    opener=build_opener(proxy_handler,cookie_handler)
    return opener
def get(url,opener):
    req=Request(url)
    resp=opener.open(req)
    with open('ip.html','wb') as f:
        f.write(resp.read())
if __name__ == '__main__':
    opener=build_browser()
    get('http://www.baidu.com',opener)