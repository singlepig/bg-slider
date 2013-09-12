#!/usr/bin/python
#-*- encoding: utf-8 -*-

import os
import random
import time

running = True

while running:
    pic_list = os.listdir('/home/singlepig/pictures/wallpapers')#壁纸目录
    pic_num = len(pic_list)#获取壁纸目录的壁纸数量
    filename = random.randint(0,pic_num)#随机选择一个壁纸在pic_list中的序号
    #print(pic_list[filename])
    os.popen('gsettings set org.gnome.desktop.background picture-uri file:///'+'home/singlepig/pictures/wallpapers/'+pic_list[filename])
    time.sleep(60*2)#休眠2分钟
