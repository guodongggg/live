from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import urllib.request
import ssl
import operator
from .spider import *
from .online_sort import *


def index(request):
    douyu_lol = Spider().douyu('lol')
    huya_lol = Spider().huya('lol')
    #panda_lol = Spider().panda('lol')
    qie_lol = Spider().qie('lol')

    # 合并多个平台
    old_infos = douyu_lol + huya_lol + qie_lol

    # 将含万的人气值转换为数字，重新进行排序
    all_infos = OnlineSort().online_change(old_infos)

    # 返回列表
    return render(request, 'index.html', {'all_infos': all_infos})


def common(request, item):
    douyu = Spider().douyu(item)
    huya = Spider().huya(item)
    qie = Spider().qie(item)

    #熊猫TV倒闭
    #panda = Spider().panda(item)

    # 合并多个平台
    old_infos = douyu + huya + qie

    # 将含万的人气值转换为数字，重新进行排序
    all_infos = OnlineSort().online_change(old_infos)

    # 返回列表
    return render(request, 'index.html', {'all_infos': all_infos})
