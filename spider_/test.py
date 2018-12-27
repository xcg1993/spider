import ssl
from urllib.parse import urlencode
from urllib.request import Request,urlopen

ssl._create_default_https_context=ssl._create_unverified_context
url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    "Connection":"keep-alive"
}
def main():
    page=2
    start=(page-1)*20
    limit=20
    data={
        'start':start,
        'limit':limit,
    }
    data=urlencode(data).encode()
    request1=Request(url,data,headers)
    response=urlopen(request1)
    print(response.read().decode())
if __name__ == '__main__':
    main()