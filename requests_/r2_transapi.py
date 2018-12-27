import re

import requests
url = 'https://fanyi.baidu.com/transapi'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=56D369559ECDD0D61E99F26EBADA0284:FG=1'
}
def transapi(keyword):
    if re.match(r'^[a-zA-Z]+$',keyword):
        from_,to_='en','zh'
    elif re.match(r'^[u4e00-\u9fa5]+$',keyword):
        from_,to_='zh','en'

    else:
        print(f'无法识别{keyword}')


    params={
        'from':from_,
        "to":to_,
        'query':keyword,
        'source':'txt'
    }
    resp=requests.post(url,params,headers=headers)
    if resp.status_code==200:
        content_type=resp.headers.get('content-type')
        if content_type.startswith('application/json'):
            json = resp.json()
            print(json)


if __name__ == '__main__':
    transapi('苹果')