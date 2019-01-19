from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    url = 'http://open.douyucdn.cn/api/RoomApi/live/1'
    r = requests.get(url)
    response_dict = r.json()
    infos = response_dict['data']

    return render(request, 'index.html', {'infos': infos})



