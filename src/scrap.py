import requests
import urllib.request
import re
import random
from time import sleep

from requests.packages.urllib3.connectionpool import xrange
from django.conf import settings

settings.configure()


def main():
    url = 'https://www.zhihu.com/question/31785374'

    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Host': 'www.zhihu.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.6',
        'Origin': 'https://www.zhihu.com/',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrftoken': '5a8f7a85b52ac238cf2f1d54a7e9058f',
        'Cookie': '_zap=86ba93c5-7f49-4765-9e63-2e1bb1022282; d_c0="AFAA2HMe0gqPTjPUBarztRa2EKs4kV1rItU=|1478679536"; _zap=801fcbdb-b557-448c-999f-ca7ef32add14; _xsrf=5a8f7a85b52ac238cf2f1d54a7e9058f; l_n_c=1; q_c1=b53847a074eb45108067e084ab2b5c51|1494215596000|1494215596000; r_cap_id="MjdjM2ExMTgzZGE5NDZjNmE2ZGI5NDViMTI2ZmUwYWY=|1494215596|3241eb0bf4c7dd2d2d6b3ab552bd6e8c9695f2dc"; cap_id="YjA5OGUxNDNjY2RmNDk5Mzk5NDkyZWNhODQxYmZiMTQ=|1494215596|8f6262e5760dba57abb4d9c59a0e859ad9fc83ac"; l_cap_id="Yjc3OTE4YTM5ZjQ0NDkyNmE2OTNjOWVlYjRkNDQ2ZjM=|1494215596|7469ebe3f01e7ec74ed841abc77b3548b491d0a3"; n_c=1; __utma=51854390.1604238998.1494215563.1494215563.1494215563.1; __utmb=51854390.0.10.1494215563; __utmc=51854390; __utmz=51854390.1494215563.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.110-1|2=registration_date=20140520=1^3=entry_date=20140520=1'
    }
    i = 1
    for x in xrange(20, 3600, 20):
        # 需要更换条件
        data = {'start': '0', 'offset': str(x), '_xsrf': '5a8f7a85b52ac238cf2f1d54a7e9058f'}
        # 知乎用offset控制加载的个数，每次响应加载20
        content = requests.get(url, headers=headers, data=data, timeout=10).text
        # 用post提交form data, 只要双斜杠就行,不要四条
        imgs = re.findall('<img src=\\"(.*?)_b.jpg', content)
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
