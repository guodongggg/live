from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import urllib.request
import ssl
import operator


def test(request, games):
    return render(request, 'test.html', {'games': games})


def index(request):
    # 斗鱼官方API接口
    url = 'http://open.douyucdn.cn/api/RoomApi/live/1'
    # 代理IP，绕过反爬防护
    # proxy = {'http': 'http://14.20.235.156:9797'}
    # proxy = {'http': 'http://112.91.218.21:9000'}
    # proxy = {'http': 'http://110.83.40.37:9999'}
    # r = requests.get(url, proxies=proxy)
    r = requests.get(url)
    response_dict = r.json()
    douyu_list = response_dict['data']

    # 虎牙
    # 通过爬虫提取直播信息
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen('https://www.huya.com/g/lol')
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

    while i < int(len(imglist)):
        zb = {}
        zb['room_name'] = namelist[i]
        zb['room_src'] = imglist[i]
        zb['nickname'] = nicklist[i]
        zb['url'] = urllist[i]
        zb['online'] = onlinelist[i]
        huya_list.append(zb)
        i += 1

    # 合并多个平台
    old_infos = douyu_list + huya_list

    # 将含万的人气值转换为数字
    def online_change(num_lists, num_key='online'):
        for num_list in num_lists:
            list_num = str(num_list[num_key])
            reg = r'(.+?)万'
            matchObj = re.match(reg, list_num)
            if matchObj:
                num_list['online'] = int(float(matchObj.group(1).strip()) * 10000)
            else:
                num_list['online'] = int(num_list['online'])
        # 按online的值大小重新排序列表
        num_lists = sorted(num_lists, key=operator.itemgetter('online'), reverse=True)
        # 大于1万人气重新加上万为单位
        for x in num_lists:
            if x[num_key] > 10000:
                x[num_key] = str(round(x[num_key] / 10000, 1)) + '万'
        return num_lists

    all_infos = online_change(old_infos)
    # 返回列表
    return render(request, 'index.html', {'all_infos': all_infos})


def common(request, item):

    # 斗鱼官方API接口
    if item == 'pubg':
        url = 'http://open.douyucdn.cn/api/RoomApi/live/270'
        response = urllib.request.urlopen('https://www.huya.com/g/2793')
    elif item == 'lol':
        url = 'http://open.douyucdn.cn/api/RoomApi/live/1'
        response = urllib.request.urlopen('https://www.huya.com/g/lol')
    # 代理IP，绕过反爬防护
    # proxy = {'http': 'http://14.20.235.156:9797'}
    # proxy = {'http': 'http://112.91.218.21:9000'}
    # proxy = {'http': 'http://110.83.40.37:9999'}
    # r = requests.get(url, proxies=proxy)
    r = requests.get(url)
    response_dict = r.json()
    douyu_list = response_dict['data']

    # 虎牙
    # 通过爬虫提取直播信息
    ssl._create_default_https_context = ssl._create_unverified_context

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

    while i < int(len(imglist)):
        zb = {}
        zb['room_name'] = namelist[i]
        zb['room_src'] = imglist[i]
        zb['nickname'] = nicklist[i]
        zb['url'] = urllist[i]
        zb['online'] = onlinelist[i]
        huya_list.append(zb)
        i += 1

    # 合并多个平台
    old_infos = douyu_list + huya_list

    # 将含万的人气值转换为数字
    def online_change(num_lists, num_key='online'):
        for num_list in num_lists:
            list_num = str(num_list[num_key])
            reg = r'(.+?)万'
            matchObj = re.match(reg, list_num)
            if matchObj:
                num_list['online'] = int(float(matchObj.group(1).strip()) * 10000)
            else:
                num_list['online'] = int(num_list['online'])
        # 按online的值大小重新排序列表
        num_lists = sorted(num_lists, key=operator.itemgetter('online'), reverse=True)
        # 大于1万人气重新加上万为单位
        for x in num_lists:
            if x[num_key] > 10000:
                x[num_key] = str(round(x[num_key] / 10000, 1)) + '万'
        return num_lists

    all_infos = online_change(old_infos)
    # 返回列表
    return render(request, 'index.html', {'all_infos': all_infos})

