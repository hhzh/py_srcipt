import re

from bs4 import BeautifulSoup
from  urllib import request


# from urllib import parse

def open_url(url):
    req = request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
    response = request.urlopen(url)
    if response.getcode() == 200:
        content = response.read()
        return content


def down_img(url):
    content = open_url(url)
    soup = BeautifulSoup(content, 'html.parser')
    urls = soup.find_all('img', src=re.compile('data-original'))
    count = 1
    for url1 in urls:
        # print(url1.get('data-original'))
        try:
            filename = 'e:/img/' + str(count) + '.jpg'
            print('正在下载：', url1.get('data-original'))
            request.urlretrieve(url1.get('data-original'), filename)
            count = count + 1
        except:
            print('这张不能下载', url1.get('data-original'))


if __name__ == '__main__':
    # con = open_url('https://www.zhihu.com/question/49075464')
    # print(con)
    down_img('https://www.zhihu.com/question/49075464')
