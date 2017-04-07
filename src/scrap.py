import requests
import urllib.request
import re
import random
from time import sleep

from requests.packages.urllib3.connectionpool import xrange
from django.conf import settings

settings.configure()


def main():
    url = 'https://www.zhihu.com/question/22867272'

    # 感觉这个话题下面美女多
    my_cookies = {"d_c0": '"ABDAR4n_PAqPTv-ONLWhQl39CMoKQ--05Wc=|1468672210"',
                  "_zap": "b9456df6-9346-4cb7-ae39-83ce8b85479b",
                  "_za": "d481f9fb-e7e5-451d-a247-2be5dcb502ca",
                  "_xsrf": "c932deb936dca94eb0486c98b331d2a3",
                  "sid": "dq5bbei2",
                  "q_c1": "51ae6f89182846f78c40f6b8adca30a6|1490371206000|1477132640000",
                  "l_cap_id": '"YWIyODU4YjQyNDNmNGJjMWFmZWMzOGQ2NzMwZWY1NmY=|1491576336|d9448372656503b31c7814c8f1dd4b50a15ef954"',
                  "cap_id": '"ZGZlYzBkNDY5M2M0NDYyYjhhODM2Yzc2ZTUyNjk2MjQ=|1491576336|81eac8f4dfc488c62195b95bf2d5b6d915975354"',
                  "__utma": "51854390.863682907.1468672209.1487475870.1491575719.37",
                  "__utmb": "51854390.0.10.1491575719",
                  "__utmc": "51854390",
                  "__utmz": "51854390.1491575719.37.34.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
                  "__utmv": "51854390.100-1|2=registration_date=20140520=1^3=entry_date=20140520=1",
                  "aliyungf_tc": "AQAAAEU7rR+sMgIAX1tH3skL4vAoHrqV",
                  "capsion_ticket": '"2|1:0|10:1491576641|14:capsion_ticket|44:YTYzYTNkNjQzODdjNGY0ZGIzNzA1ZjYyMWIxYWZmMDE=|be16c164a7ff3da3ad86c11814ed09c6c3f4ff09798291896b181bbbf35e6bc3"',
                  "l_n_c": "1",
                  "r_cap_id": "MzE4YTc0MzEwOTZmNDRmM2FkMDM2ZTk3YzgwM2JkMmE=|1491576336|598e86c3fce3a5d2add8d4d901e82b4db203cb1a",
                  "s-i": "10",
                  "s-q": "Python%20%E7%88%AC%E7%9F%A5%E4%B9%8E%E5%A4%B4%E5%83%8F",
                  "z_c0": "Mi4wQUFDQW0xUXZBQUFBRU1CSGlmODhDaGNBQUFCaEFsVk5VVFFQV1FEeXdfNGV6MHFqZ2wyU2JHWXpXcTF5djY3NEhB|1491576660|7acbbac915a6983fdc85049333555f4a366a38be",
                  "n_c": "1"}
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Host': 'www.zhihu.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.6',
        'Origin': 'https://www.zhihu.com/',
        'Connection': 'keep-alive',
        'Referer': 'https://www.zhihu.com/question/56748730',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrftoken': 'c932deb936dca94eb0486c98b331d2a3',
        'Cookie': '__utma=51854390.863682907.1468672209.1487475870.1491575719.37;__utmb=51854390.0.10.1491575719;__utmc=51854390;__utmv=51854390.100-1|2=registration_date=20140520=1^3=entry_date=20140520=1;			__utmz=51854390.1491575719.37.34.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;			_xsrf=c932deb936dca94eb0486c98b331d2a3;		_za=d481f9fb-e7e5-451d-a247-2be5dcb502ca;			_zap=b9456df6-9346-4cb7-ae39-83ce8b85479b;		aliyungf_tc=AQAAAEU7rR+sMgIAX1tH3skL4vAoHrqV;	cap_id="ZGZlYzBkNDY5M2M0NDYyYjhhODM2Yzc2ZTUyNjk2MjQ=|1491576336|81eac8f4dfc488c62195b95bf2d5b6d915975354";capsion_ticket="2|1:0|10:1491576641|14:capsion_ticket|44:YTYzYTNkNjQzODdjNGY0ZGIzNzA1ZjYyMWIxYWZmMDE=|be16c164a7ff3da3ad86c11814ed09c6c3f4ff09798291896b181bbbf35e6bc3";d_c0="ABDAR4n_PAqPTv-ONLWhQl39CMoKQ--05Wc=|1468672210";		l_cap_id="YWIyODU4YjQyNDNmNGJjMWFmZWMzOGQ2NzMwZWY1NmY=|1491576336|d9448372656503b31c7814c8f1dd4b50a15ef954";l_n_c=1;		n_c=1;q_c1=51ae6f89182846f78c40f6b8adca30a6|1490371206000|1477132640000;			r_cap_id="MzE4YTc0MzEwOTZmNDRmM2FkMDM2ZTk3YzgwM2JkMmE=|1491576336|598e86c3fce3a5d2add8d4d901e82b4db203cb1a";s-i=10;	s-q=Python%20%E7%88%AC%E7%9F%A5%E4%B9%8E%E5%A4%B4%E5%83%8F;		sid=dq5bbei2;z_c0=Mi4wQUFDQW0xUXZBQUFBRU1CSGlmODhDaGNBQUFCaEFsVk5VVFFQV1FEeXdfNGV6MHFqZ2wyU2JHWXpXcTF5djY3NEhB|1491579339|b6376a9a195550383bb1019b64d93976a2bf8d42'}
    i = 1
    for x in xrange(20, 3600, 20):
        # 需要更换条件
        data = {'start': '0', 'offset': str(x), '_xsrf': 'c932deb936dca94eb0486c98b331d2a3'}
        # 知乎用offset控制加载的个数，每次响应加载20
        content = requests.get(url, headers=headers, data=data, timeout=10).text
        # 用post提交form data, 只要双斜杠就行,不要四条
        imgs = re.findall(
            '<img class=\\"Avatar AuthorInfo-avatar\\" style=\\"width:38px;height:38px;\\" src=\\"(.*?)_xs.jpg',
            content)
        print(imgs)
        # 在爬下来的json上用正则提取图片地址，去掉_m为大图
        for img in imgs:
            # noinspection PyBroadException
            try:
                img = img.replace('\\', '')
                # 去掉\字符这个干扰成分
                pic = img + '.jpg'
                print(pic)
                # 需要先建文件夹
                path = 'D:\\pics\\' + '%s.jpg' % i
                # 声明存储地址及图片名称
                urllib.request.urlretrieve(pic, path)  # python 3
                # 下载图片
                print('下载了第' + str(i) + u'张图片')
                i += 1
                sleep(random.uniform(1, 3))
                # 睡眠函数用于防止爬取过快被封IP
            except:
                print('抓漏1张')
            pass
        sleep(random.uniform(0.5, 1))


if __name__ == '__main__':
    main()
