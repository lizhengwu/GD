#!/usr/bin/python3

from common import PATH
from random import choice, randint

# 获取随机目标数值
def getRandomTargetData():
    data = []
    for _ in range(6):
        d = {
            'name': choice(PATH),
            'target': randint(51, 100)
        }
        data.append(d)
    
    for item in data:
        print(item)


if __name__ == "__main__":
    getRandomTargetData()