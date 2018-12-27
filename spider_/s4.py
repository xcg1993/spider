"""
post,定制headers请求头
1.urllib.request.Resquest(url,data,headers)
data 如果不为空，表示Request的方法是post,反之为
Get
2.针对data数据进行urlencode编码
"""
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': 'BAIDUID=56D369559ECDD0D61E99F26EBADA0284:FG=1; BIDUPSID=56D369559ECDD0D61E99F26EBADA0284; PSTM=1544583304; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=26523_1435_21079_18559_28132_27751_28140_27509; PSINO=1; locale=zh; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1545206785,1545206806,1545208808,1545209720; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1545209720'
}

url = 'https://fanyi.baidu.com/v2transapi'


def main(word, from_lang, to_lang):
    data = {
        'from': from_lang,
        'to': to_lang,
        'query': word,
        # 'transtype': 'translang',
        'simple_means_flag': 3,
        'sign': 897527.611014,
        'token': 'faa9087cd3bd12823426b15e05a26383'
    }
    # 生成post请求
    # data是from=en&to=zh字节码
    request = Request(url, urlencode(data).encode(), headers)
    try:
        resp = urlopen(request)
        # print(type(resp))
        # json.loads()将json格式字符串转为dict或list
        json_ = json.loads(resp.read().decode())
        # print(resp.read())
        print(json_)
    except:
        pass


if __name__ == '__main__':
    main('水', 'zh', 'en')
