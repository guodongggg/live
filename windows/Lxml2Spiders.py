import urllib.request
import ssl
from lxml import etree


def HtmlString(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    return content


def huya(url):
    content = HtmlString(url)
    result = etree.HTML(content)
    main_xpath = '//*[@id="js-live-list"]/li[@class="game-live-item"]'
    img_xpath = main_xpath + '/a[@class="video-info "]/img/@*'
    name_xpath = main_xpath + '/a[@class="title"]/@title'
    nick_xpath = main_xpath + '/span/span[@class="avatar fl"]/i/@title'
    online_xpath = main_xpath + '/span/span[@class="num"]/i[@class="js-num"]/text()'
    url_xpath = main_xpath + '/a[@class="video-info "]/@href'

    imglist = result.xpath(img_xpath)
    namelist = result.xpath(name_xpath)
    nicklist = result.xpath(nick_xpath)
    onlinelist = result.xpath(online_xpath)
    urllist = result.xpath(url_xpath)

    # 由于lxml属性值无法静态取到直播间截图url，故做此处理
    img_tmp = []
    for i in range(1, len(imglist), 6):
        img_tmp.append(imglist[i])
    imglist = img_tmp

    alldata = {}
    alldata['imglist'] = imglist
    alldata['namelist'] = namelist
    alldata['nicklist'] = nicklist
    alldata['onlinelist'] = onlinelist
    alldata['urllist'] = urllist

    return alldata


if __name__ == '__main__':
    l = huya('http://www.huya.com/g/lol')
    print(l['imglist'][0])
    print(l['namelist'][0])
    print(l['nicklist'][0])
    print(l['onlinelist'][0])
    print(l['urllist'][0])