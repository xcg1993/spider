from urllib.request import Request, urlopen

url='http://www.renren.com/722910827'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Cookie':'ick_login=6adcd78a-ccd2-4c1e-9590-4602897dd4be; anonymid=jpw0rfta-wz97i7; depovince=GW; jebecookies=9c3129a0-896e-4da4-86fd-ab20522c3224|||||; _r01_=1; JSESSIONID=abc_w4m2AEv1g6XS1JjFw; jebe_key=e35e7ee1-810f-4b18-9051-c25516fbc2e7%7C62469123fef20f5e0653f13d92e8a390%7C1545274977120%7C1%7C1545274962068; _de=A4D1A7A2C20F1AF7303554EBBEB4676C696BF75400CE19CC; p=69bfb8041afefd7702dc56484809e00c7; first_login_flag=1; ln_uact=770527054@qq.com;ln_hurl=http://hdn101.rrimg.com/photos/hdn101/20090701/20/55/head_78Yj_31643c241039.jpg; t=d31f74e2c008c66b99005776874d826c7;societygueste=d31f74e2c008c66b99005776874d826c7; id=722910827; xnsid=366f1e8d; loginfrom=null; ch_id=10016; wp_fold=0; ver=7.0'
}

req=Request(url,headers=headers)
resp=urlopen(req)
with open('resp3.html','wb') as f:
    f.write(resp.read())

print('ok')