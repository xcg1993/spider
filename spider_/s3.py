'''
quote将中文进行url编码
unquote:将url进行解码
urlencode:将完整的url中的参数进行编码
'''
from urllib.parse import quote,urlencode,unquote
from urllib.request import urlopen,urlretrieve
def test():
    data={
        'word':'菊花',
        'tn':'baiduimge'
    }
    print(urlencode(data))





def baidu_search(keyword):
    encode_params='word=%E7%BE%8E%E9%A3%9F1'
    #url='https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E7%BE%8E%E9%A3%9F&step_word=&hs=2&pn=3&spn=0&di=1064504670&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3314782076%2C3148103398&os=3499046438%2C769475572&simid=1905339633%2C748525182&adpicid=0&lpn=0&ln=1967&fr=&fmq=1545204229906_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=13&oriquery=&objurl=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Fc995d143ad4bd113ddcfb60e51afa40f4bfb058f.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Frwtxtg_z%26e3Bv54AzdH3Fri5p5v5ry6t2ipAzdH3F8ndlnadl9&gsm=0&rpstart=0&rpnum=0&islist=&querylist='

    params=unquote(encode_params)
    print(params)



if __name__ == '__main__':
    #baidu_search(1)
    test()