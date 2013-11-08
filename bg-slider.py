#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import os
import random
import time
import subprocess

def visitDir(arg, dirname, names):
    for filespath in names:
        fullpath = os.path.join(dirname, filespath)  # 显示出文件的绝对路径
        if os.path.isdir(fullpath) is False:
            # 判断是否为目录，若不是目录则加入list
            pic_list.append(fullpath)

if __name__ == "__main__":
    pic_base_path = '/home/singlepig/picture/wallpapers'   # step 1
    #壁纸文件所在的目录，程序会搜索该目录下的所有子目录
    pic_list = []
    os.path.walk(pic_base_path,visitDir,())
    pic_num = len(pic_list)  # 获取壁纸目录的壁纸数量

    while True:
        fileNum = random.randint(0,pic_num)  # 随机选择一个壁纸在pic_list中的序号
        print "=============="
        print pic_list[fileNum]
        bashCom = 'gsettings set org.gnome.desktop.background picture-uri file://' + pic_list[fileNum]
        #bashCom = r'gsettings set org.gnome.desktop.background picture-uri file:///home/singlepig/picture/wallpapers/拳皇街霸/KOF (11).jpg'
        #os.popen(bashCom)
        ps = subprocess.Popen(bashCom, shell=True)
        ps.wait()
        #print bashCom
        print "===set over==="
        # step 2
        time.sleep(60)
        #休眠1分钟
