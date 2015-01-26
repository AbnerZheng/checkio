#coding=utf8
__author__ = '璐'

def checkio(data):
    if data:
        return data.pop() + checkio(data)
    else:
        return 0
