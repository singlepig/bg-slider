#!/usr/bin/python
#-*- encoding: utf-8 -*-

import threading
import urllib
import re
import os
import time

# Change Point 1 -下载目录，手动填写，若不存在则会自动创建文件夹，dont worry！
download_dir = '/home/singlepig/temp/imgs/进击的巨人壁纸'
if os.path.exists(download_dir) == False:
    os.mkdir(download_dir)

# Change Point 2 -设定要下载的壁纸的分辨率
width = 1366
height = 768

# Change Point 3 -需要爬的网页url，自行更换,末尾的'/'不能少!
source_html = 'http://m.lovebizhi.com/category/21733/'



# Change Point 4 -此tag也需要根据特定情况修改alt部分
tag = r'<img alt="进击的巨人壁纸" src="(.*?)"/>'
pattern = re.compile(tag)
'''
在
<li class="s_big"><a href="/share/1119685" title="所属分类：网络热词"><img alt="网络热词壁纸" src="http://s.qdcdn.com/cl/11512075,400,300.jpg"/></a></li>
中匹配出图片url
'''

#记录图片编号
serial_number = []
#多线程列表
task_list = []
# Change Point 5 -最大并发线程数
max_thread = 4  #question:实际运行时貌似最大线程数是6

def creat_thread(html):
    html_source_code = urllib.urlopen(html).read() #获取目标网页源码'http://m.lovebizhi.com/category/13486/'
    items = pattern.findall(html_source_code) #用RE找到所有匹配的图片url,'http://s.qdcdn.com/cl/11512075,400,300.jpg'
    if items != []:
        for n in range(len(items)):
            target_url = 'http://s.qdcdn.com/cl/' + fix_file_name(items[n])
            task = threading.Thread(target = down_img, args = (target_url, serial_number[-1] + '.jpg'))
            #添加线程任务，调用down_img函数
            task_list.append(task)
            #加入task_list列表
    else:
        print "未找到符合的壁纸url！请确认source_html!"
        page_avaliable = False #表示出错

def down_img(url,name):
    #下载函数
    urllib.urlretrieve(url,os.path.join(download_dir,name))
    lock.release()
    print "有 ",threading.activeCount(),"个线程在运行中"
    print 'Img ' + name + ' is done! Location = ' + download_dir 

def fix_file_name(origin_url): #处理并返回新的文件名'11512075,1366,768.jpg'
    file_name = origin_url.split('/')[-1] #分解img文件的url，获取文件名和后缀名,如 '11512075,400,300.jpg'
    split_file_name = file_name.split(',') #分解文件名，得到['11512075', '400', '300.jpg']
    serial_number.append(split_file_name[0]) #得到图片的编号'11512075',并加入全局变量serial_number中
    return serial_number[-1] + ',' + str(width) + ',' + str(height) + '.jpg'


def main():
    page_avaliable = True
    # 爬取深度default,爬取过程中自增
    page = 1  # http://m.lovebizhi.com/category/844/x
    creat_thread(source_html + str(page))
    while page_avaliable == True:
        for task in task_list:
            #启动线程
            lock.acquire()
            print "有 ",threading.activeCount(),"个线程在运行中"
            task.start()
            print str(task) + ' is started!'
            time.sleep(0.5)

        for task in task_list:
            #等待线程退出
            task.join(20)
            print str(task) + ' wait to exit.'
            print "有 ",threading.activeCount(),"个线程在运行中"
        
        page = page + 1
        creat_thread(source_html + str(page))

    print 'All Done!'


if __name__ == '__main__':
    lock = threading.BoundedSemaphore(max_thread) #设置有限信号量为最大线程数，即release()-acquire()的差值,默认为1
    
    main()
    
    print "!!!有 ",threading.activeCount(),"个线程在运行中"
