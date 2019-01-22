from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import urllib.request
import ssl

def index(request):
    # 斗鱼官方的API接口
    url = 'http://open.douyucdn.cn/api/RoomApi/live/1'
    r = requests.get(url)
    response_dict = r.json()
    infos = response_dict['data']

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
        zb['name'] = namelist[i]
        zb['img'] = imglist[i]
        zb['nick'] = nicklist[i]
        zb['url'] = urllist[i]
        zb['online'] = onlinelist[i]
        huya_list.append(zb)
        i += 1

    # 返回列表
    return render(request, 'index.html', {'infos': infos, 'huya_list': huya_list})



