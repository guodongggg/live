import urllib.request
import ssl
from lxml import etree


def HtmlString(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    return content


def CollectData(img_xpath, name_xpath, nick_xpath, online_xpath, url_xpath,result):
    imglist = result.xpath(img_xpath)
    namelist = result.xpath(name_xpath)
    nicklist = result.xpath(nick_xpath)
    onlinelist = result.xpath(online_xpath)
    urllist = result.xpath(url_xpath)

    alldata = {}
    alldata['imglist'] = imglist
    alldata['namelist'] = namelist
    alldata['nicklist'] = nicklist
    alldata['onlinelist'] = onlinelist
    alldata['urllist'] = urllist

    return alldata

def huya(url):
    content = HtmlString(url)
    result = etree.HTML(content)

    main_xpath = '//*[@id="js-live-list"]/li[@class="game-live-item"]'
    img_xpath = main_xpath + '/a[@class="video-info "]/img/@*'
    name_xpath = main_xpath + '/a[@class="title"]/@title'
    nick_xpath = main_xpath + '/span/span[@class="avatar fl"]/i/@title'
    online_xpath = main_xpath + '/span/span[@class="num"]/i[@class="js-num"]/text()'
    url_xpath = main_xpath + '/a[@class="video-info "]/@href'

    huyadata = CollectData(img_xpath, name_xpath, nick_xpath, online_xpath, url_xpath, result)

    # 由于lxml属性值无法静态取到直播间截图url，故做此处理
    img_tmp = []
    for i in range(1, len(huyadata['imglist']), 6):
        img_tmp.append(huyadata['imglist'][i])
    huyadata['imglist'] = img_tmp

    return huyadata


def qie(url):
    content = HtmlString(url)
    result = etree.HTML(content)

    main_xpath = '//*[@id="__layout"]/div/div[2]/div[2]/ul/li[@class="gui-list-normal gui-list-percent"]'
    img_xpath = main_xpath + '/a/div[@class="content"]/img/@src'
    name_xpath = main_xpath + '/a/@title'
    nick_xpath = main_xpath + '/a/div[@class="info-anchor"]/p/text()'
    online_xpath = main_xpath + '/a/div[@class="info-anchor"]/span/text()'
    url_xpath = main_xpath + '/a/@href'

    qiedata = CollectData(img_xpath, name_xpath, nick_xpath, online_xpath, url_xpath, result)

    # 修改没有配置房间首页的图像地址为默认
    default_img = '../static/images/qie_background.png'
    temp = [default_img if '.jpg' in i else i for i in qiedata['imglist']]
    qiedata['imglist'] = temp

    return qiedata


def bilibili(url):
    content = HtmlString(url)
    result = etree.HTML(content)

    main_xpath = ''    
    img_xpath = main_xpath + ''
    name_xpath = main_xpath + ''
    nick_xpath = main_xpath + ''
    online_xpath = main_xpath + ''
    url_xpath = main_xpath + ''

    bilibilidata = CollectData(img_xpath, name_xpath, nick_xpath, online_xpath, url_xpath, result)

    return bilibilidata


def douyu(url):
    content = HtmlString(url)
    result = etree.HTML(content)

    main_xpath = ''    
    img_xpath = main_xpath + ''
    name_xpath = main_xpath + ''
    nick_xpath = main_xpath + ''
    online_xpath = main_xpath + ''
    url_xpath = main_xpath + ''

    douyudata = CollectData(img_xpath, name_xpath, nick_xpath, online_xpath, url_xpath, result)

    return douyudata


if __name__ == '__main__':
    url1 = 'https://www.huya.com/g/lol'
    url2 = 'https://egame.qq.com/livelist?layoutid=lol'
    l = qie(url2)
    print((l['imglist']))
