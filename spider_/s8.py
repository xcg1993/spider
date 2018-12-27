from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener
from http.cookiejar import CookieJar

url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20181141452439'
params = {
    'email': 'zhangyan100501@163.com',
    'icode': '',
    'origURL': 'http://www.renren.com/',
    'domail': 'www.renren.com',
    'key_id': 1,
    'captcha_type': 'web_login',
    'password': '8268f673a8680c25fc8f40b50e6bc0b28a5fdb8b721f89549478be191249fd6a',
    'rkey': '39b392090c635431e86ef76d46f31f40',
    'f': ''
}
headers = {
    'User-Agent': 'QF-XA-PY05-Spider'

}


def build_broswer():
    # 1.创建Handler
    handler = HTTPCookieProcessor(CookieJar())  # 保留cookie信息的服务器
    return build_opener(handler)


def login(opener):
    req = Request(url, urlencode(params).encode(), headers)
    resp = opener.open(req)
    resp_txt = resp.read()
    print(resp_txt.decode())


def home(opener):
    resp=opener.open('http://www.renren.com/')

    with open('renren.html','wb') as f:
        f.write(resp.read())
if __name__ == '__main__':
    browser = build_broswer()
    login(browser)
    home(browser)
