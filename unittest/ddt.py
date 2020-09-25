'''
@author: lixuewen
@file: ddt.py
@time: 2020/9/25 10:48
@desc:
'''

def data(list):
    def wrapper(function):
        def inner(self):
            for data in list:
                function(self,*data)
        return inner
    return wrapper