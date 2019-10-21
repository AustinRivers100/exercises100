# -*- coding: utf-8 -*-
while True:
    year = int(input('请输入一个1000到2000之间年份，系统帮你判断是否为闰年：'))
    if 1000 <= year <= 2000:
        if year % 100 == 0 and year % 400 == 0: #世纪年除以400，能除尽则为闰年
            print('这是一个闰年')
        elif year % 100 != 0 and year % 4 == 0:  #普通年除以4,能除尽则为闰年
            print('这是一个闰年')
        else:
            print('这不是一个闰年')
    else:
        print('你输入的不是指定年份，请重新输入')