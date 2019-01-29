# 将抓取的列表中的字典的人气值一列按大小重新进行排序

import operator
import re


class OnlineSort():

    def online_change(self, num_lists, num_key='online'):
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
