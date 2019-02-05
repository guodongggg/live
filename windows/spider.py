import requests
import re
import urllib.request
import ssl

douyu_kv = {'lol': '1', 'pubg': '270', 'dnf': '40', 'dota2': '3', 'hearthstone': '2', 'csgo': '6',
            'hmoeconsole': '19', 'overwatch': '148'}
huya_kv = {'lol': 'lol', 'pubg': '2793', 'dnf': 'dnf', 'dota2': 'dota2', 'hearthstone': 'hearthstone',
           'csgo': '862', 'hmoeconsole': '100032', 'overwatch': 'overwatch'}
panda_kv = {'lol': 'lol'}
qie_kv = {'lol': 'lol'}


class Spider():

    def panda(self, game):
        # 熊猫直播
        url = 'https://www.panda.tv/cate/%s' % panda_kv[game]
        # 通过爬虫提取直播信息
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        # file_path = 'D:\Python\爬虫\虎牙\panda.txt'
        # with open(file_path) as file_object:
        #     content = file_object.read()

        reg_img = r'data-original="(.+?)" alt="'
        reg_name = r'<span class="video-title" title="(.+?)">'
        reg_nick = r'class="video-nickname" title="(.+?)">'
        reg_online = r'<i class="ricon ricon-eye"></i>(.+?)</span>'
        reg_url = r'href="(.+?)" class="video-list-item-wrap"'

        reg_IMG = re.compile(reg_img)  # 编译一下，运行更快
        reg_NAME = re.compile(reg_name)
        reg_NICK = re.compile(reg_nick)
        reg_ONLINE = re.compile(reg_online)
        reg_URL = re.compile(reg_url)

        imglist = reg_IMG.findall(content)
        namelist = reg_NAME.findall(content)  # 进行匹配
        nicklist = reg_NICK.findall(content)
        onlinelist = reg_ONLINE.findall(content)
        urllist = reg_URL.findall(content)

        i = 0
        info_list = []

        # 抓取所有的房间
        # while i < int(len(namelist)):
        while i < 30:
            zb = {}
            zb['room_name'] = namelist[i]
            zb['room_src'] = imglist[i]
            zb['nickname'] = nicklist[i]
            zb['url'] = "http://www.panda.tv" + urllist[i]
            zb['online'] = onlinelist[i]
            zb['platform'] = '熊猫'
            info_list.append(zb)
            i += 1
        return info_list

    def qie(self, game):
        # 企鹅电竞
        url = 'https://egame.qq.com/livelist?layoutid=%s' % qie_kv[game]
        # 通过爬虫提取直播信息
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        # file_path = 'D:\Python\爬虫\虎牙\qie.txt'
        # with open(file_path) as file_object:
        #     content = file_object.read()

        reg_img = r' <img src="(.+?)" alt="'
        reg_name = r'<h4 class="info-livename">(.+?)</h4>'
        reg_nick = r'><p class="name">(.+?)</p> '
        reg_online = r'VORK5CYII=">([\s\S]*?)</span></div></a>'
        reg_url = r'<a href="(.+?)" target="_blank" title="'

        reg_IMG = re.compile(reg_img)  # 编译一下，运行更快
        reg_NAME = re.compile(reg_name)
        reg_NICK = re.compile(reg_nick)
        reg_ONLINE = re.compile(reg_online)
        reg_URL = re.compile(reg_url)

        imglist = reg_IMG.findall(content)
        namelist = reg_NAME.findall(content)  # 进行匹配
        nicklist = reg_NICK.findall(content)
        onlinelist = reg_ONLINE.findall(content)
        urllist = reg_URL.findall(content)

        i = 0
        info_list = []

        # while i < int(len(namelist)):
        while i < 30:
            zb = {}
            zb['room_name'] = namelist[i]
            zb['room_src'] = imglist[i]
            zb['nickname'] = nicklist[i]
            zb['url'] = "https://egame.qq.com" + urllist[i]
            zb['online'] = onlinelist[i].replace('\n', '').replace(' ', '')
            zb['platform'] = '企鹅电竞'
            info_list.append(zb)
            i += 1
        return info_list

    def douyu(self, game):
        url = 'http://open.douyucdn.cn/api/RoomApi/live/%s' % douyu_kv[game]
        # 斗鱼官方API接口
        # url = 'http://open.douyucdn.cn/api/RoomApi/live/1'
        # 代理IP，绕过反爬防护
        # proxy = {'http': 'http://14.20.235.156:9797'}
        # proxy = {'http': 'http://112.91.218.21:9000'}
        # proxy = {'http': 'http://110.83.40.37:9999'}
        # r = requests.get(url, proxies=proxy)
        r = requests.get(url)
        response_dict = r.json()
        douyu_list = response_dict['data']
        for detail in douyu_list:
            detail['platform'] = '斗鱼'
        return douyu_list

    def huya(self, game):
        url = 'https://www.huya.com/g/%s' % huya_kv[game]
        # 虎牙
        # 通过爬虫提取直播信息
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        # print(content)
        reg_img = r'class="pic" data-original="(.+?)" src='
        reg_name = r'title="(.+?)" target="_blank">'
        reg_nick = r'<i class="nick" title="(.+?)">'
        reg_online = r'<i class="js-num">(.+?)</i></span>'
        reg_url = r'<a href="(.+?)" class="title new-clickstat"'

        reg_IMG = re.compile(reg_img)  # 编译一下，运行更快
        reg_NAME = re.compile(reg_name)
        reg_NICK = re.compile(reg_nick)
        reg_ONLINE = re.compile(reg_online)
        reg_URL = re.compile(reg_url)

        imglist = reg_IMG.findall(content)
        namelist = reg_NAME.findall(content)  # 进行匹配
        nicklist = reg_NICK.findall(content)
        onlinelist = reg_ONLINE.findall(content)
        urllist = reg_URL.findall(content)

        i = 0
        huya_list = []

        # while i < int(len(imglist)):
        while i < 30:
            zb = {}
            zb['room_name'] = namelist[i]
            zb['room_src'] = imglist[i]
            zb['nickname'] = nicklist[i]
            zb['url'] = urllist[i]
            zb['online'] = onlinelist[i]
            zb['platform'] = '虎牙'
            huya_list.append(zb)
            i += 1
        return huya_list


if __name__ == '__main__':
    pass
    # x = Spider().huya('lol')
    # print(x[29])
