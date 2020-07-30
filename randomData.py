#!/usr/bin/python3

from common import PATH
from random import choice, randint

# 随机数范围
targetRangeBegin = 51
targetRangeEnd = 100
easyRangeEnd = 50

def getRandomTargetData():
    data = []

    for _ in range(6):
        targetName = choice(PATH)
        targetValue = randint(targetRangeBegin, targetRangeEnd)
        # 除目标路径外的其他路径
        easyPath = []
        difficultPath = []
        for item in PATH:
            easy = {}
            difficult = {}
            if item != targetName:
                # 简单的数据
                easy['name'] = item
                easy['value'] = randint(0, easyRangeEnd)
                # 困难的数据
                difficult['name'] = item
                difficult['value'] = randint(targetValue - 2, targetValue - 1)
            else:
                # 简单的数据
                easy['name'] = targetName
                easy['value'] = targetValue
                # 困难的数据
                difficult['name'] = targetName
                difficult['value'] = targetValue
            easyPath.append(easy)
            difficultPath.append(difficult)

        d = {
            'target_name': targetName,
            'target_value': targetValue,
            'easy': easyPath,
            'difficult': difficultPath
        }
        data.append(d)

    return data

def getData():
    serializeData = []
    targetData = getRandomTargetData()
    for item in targetData:
        _data = {
            'data_type': 'easy',
            'target_name': item.get('target_name'),
            'target_value': item.get('target_value'),
            'data': item.get('easy')
        }
        serializeData.append(_data)
    for item in targetData:
        _data = {
            'data_type': 'difficult',
            'target_name': item.get('target_name'),
            'target_value': item.get('target_value'),
            'data': item.get('difficult')
        }
        serializeData.append(_data)

    return serializeData


if __name__ == "__main__":
    data = getData()
    print(data)
