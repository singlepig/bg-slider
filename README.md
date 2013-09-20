# Introduce:
name = biubiu
type = python
自用的`ubuntu 13.04`自动换壁纸程序。适用于Gnome 3。

# Usage(用法):

```
git clone https://github.com/singlepig/background-slider.git
``` 
打开bg-slider.py文件，修改`step 1`和`step 2`,根据自己的情况选择是否更改`#!/usr/bin/python `

运行bg-slider.py.

### 支持:
2013/9/20:
1. 遍历制定目录下所有文件和文件夹
2. 随即选择壁纸文件

### 缺点:
2013/9/20:
1. 无cli
2. 若文件太大，程序速度会大降。实测3800个壁纸，检索速度略慢，建议更换时间选长点，不宜少于30s，以免拖累系统。


### coming soon:
1. 改善数据结构以加快程序运行
2. 增加cli
3. 增加随机选择子目录，随机或顺序更换目录下壁纸文件。
