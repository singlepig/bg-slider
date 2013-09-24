#!/usr/bin/python 
#-*- encoding: utf-8 -*-

import os
import random
import time

def visitDir(arg,dirname,names):
    for filespath in names:
        fullpath = os.path.join(dirname,filespath)  #显示出文件的绝对路径
        if os.path.isdir(fullpath) == False:
            #判断是否为目录，若不是目录则加入list
            pic_list.append(fullpath)

if __name__=="__main__":
    pic_base_path = '/home/singlepig/pictures/wallpapers'   # step 1
    #壁纸文件所在的目录，程序会搜索该目录下的所有子目录
    pic_list = []
    os.path.walk(pic_base_path,visitDir,())

    while True:
        pic_num = len(pic_list) #获取壁纸目录的壁纸数量
        filename = random.randint(0,pic_num)    #随机选择一个壁纸在pic_list中的序号
        os.popen('gsettings set org.gnome.desktop.background picture-uri file://' + pic_list[filename])
        # step 2
        time.sleep(60) 
        #休眠1分钟
